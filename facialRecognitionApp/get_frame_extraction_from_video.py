import cv2
import os
import argparse
from glob import glob

def extract_frames_from_video(video_path, out_dir, skip):
    """Extracts frames from one video, saving every `skip`th frame."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Cannot open {video_path}")
        return 0

    os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(video_path))[0]
    count = 0     # total frames seen
    saved = 0     # frames written

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % skip == 0:
            img_name = f"{base}_{saved+1:04d}.jpg"
            cv2.imwrite(os.path.join(out_dir, img_name), frame)
            saved += 1

        count += 1

    cap.release()
    print(f"✅ {saved} frames saved from {os.path.basename(video_path)}")
    return saved

def main(input_dir, known_dir, subject, skip):
    # pattern matches any .avi in input_dir
    video_files = glob(os.path.join(input_dir, f"{subject}_*.avi"))
    if not video_files:
        print(f"⚠️  No videos found for subject '{subject}' in {input_dir}")
        return

    out_dir = os.path.join(known_dir, subject)
    total = 0
    for vid in video_files:
        total += extract_frames_from_video(vid, out_dir, skip)

    print(f"\n🎉 Done! Extracted {total} images into '{out_dir}'.")

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Extract frames from your raw face-recording videos"
    )
    p.add_argument("input_dir",
                   help="Folder with your .avi files (e.g. data/raw)")
    p.add_argument("known_dir",
                   help="Root folder for known faces (e.g. data/known)")
    p.add_argument("subject",
                   help="Subject name (must match prefix of your .avi files)")
    p.add_argument("--skip", type=int, default=5,
                   help="Save one frame every N frames (default 5)")
    args = p.parse_args()

    main(args.input_dir, args.known_dir, args.subject, args.skip)
