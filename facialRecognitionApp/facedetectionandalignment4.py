import os
import math
import cv2
import numpy as np
import face_recognition

# --- CONFIG ---
INPUT_DIR  = "data/known"      # or "data/unknown"
OUTPUT_DIR = "data/processedboundingboxes"  # will be created if needed
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}

# margin around the face box (as fraction of box size)
MARGIN = 0.2

# target output size
TARGET_SIZE = (160, 160)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def get_eye_centers(landmarks):
    # landmarks['left_eye'] and ['right_eye'] are lists of (x,y) points
    left = np.mean(landmarks["left_eye"], axis=0)
    right = np.mean(landmarks["right_eye"], axis=0)
    return tuple(left.astype(int)), tuple(right.astype(int))


def align_and_crop(image, bbox, landmarks):
    top, right, bottom, left = bbox
    # compute eye centers
    left_eye, right_eye = get_eye_centers(landmarks)
    # angle to rotate by (in degrees)
    dy = right_eye[1] - left_eye[1]
    dx = right_eye[0] - left_eye[0]
    angle = math.degrees(math.atan2(dy, dx))
    # center of rotation: midpoint between eyes
    eyes_center = ((left_eye[0] + right_eye[0]) // 2,
                   (left_eye[1] + right_eye[1]) // 2)
    # get rotation matrix
    M = cv2.getRotationMatrix2D(eyes_center, angle, 1.0)
    h, w = image.shape[:2]
    # rotate whole image
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC)
    # apply M to the bbox corners to get new box
    corners = np.array([
        [left,  top],
        [right, top],
        [right, bottom],
        [left,  bottom]
    ])
    ones = np.ones((4,1))
    pts = np.hstack([corners, ones])
    rotated_corners = M.dot(pts.T).T
    xs = rotated_corners[:,0]
    ys = rotated_corners[:,1]
    x1, x2 = int(xs.min()), int(xs.max())
    y1, y2 = int(ys.min()), int(ys.max())
    # add margin
    w_box = x2 - x1
    h_box = y2 - y1
    x1m = max(0, x1 - int(MARGIN * w_box))
    y1m = max(0, y1 - int(MARGIN * h_box))
    x2m = min(w-1, x2 + int(MARGIN * w_box))
    y2m = min(h-1, y2 + int(MARGIN * h_box))
    # crop and resize
    face = rotated[y1m:y2m, x1m:x2m]
    face = cv2.resize(face, TARGET_SIZE)
    return face


def process_folder(input_root, output_root):
    for person in os.listdir(input_root):
        in_person_dir  = os.path.join(input_root, person)
        out_person_dir = os.path.join(output_root, person)
        if not os.path.isdir(in_person_dir):
            continue
        ensure_dir(out_person_dir)

        for fname in os.listdir(in_person_dir):
            ext = os.path.splitext(fname)[1].lower()
            if ext not in IMAGE_EXTS:
                continue

            img_path = os.path.join(in_person_dir, fname)
            img = face_recognition.load_image_file(img_path)
            # 1) detect all face locations
            boxes = face_recognition.face_locations(img, model="hog")  
            # you can try model="cnn" if you have GPU
            # 2) get landmarks for each face
            landmarks_list = face_recognition.face_landmarks(img, boxes)

            for i, (box, landmarks) in enumerate(zip(boxes, landmarks_list)):
                aligned = align_and_crop(img, box, landmarks)
                out_fname = f"{os.path.splitext(fname)[0]}_face{i}{ext}"
                out_path = os.path.join(out_person_dir, out_fname)
                # convert RGB (face_recognition) → BGR (cv2) for saving
                aligned_bgr = cv2.cvtColor(aligned, cv2.COLOR_RGB2BGR)
                cv2.imwrite(out_path, aligned_bgr)
                print(f"Saved aligned face to {out_path}")


if __name__ == "__main__":
    ensure_dir(OUTPUT_DIR)
    # process both known and unknown if you like:
    process_folder("data/known", OUTPUT_DIR + "/known")
    process_folder("data/unknown", OUTPUT_DIR + "/unknown")
