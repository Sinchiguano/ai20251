import cv2
import os
import numpy as np

def preprocess_image(img_path, size=(160, 160)):
    """
    1. Loads an image from disk.
    2. Converts BGR→RGB.
    3. Resizes to `size`.
    4. Normalizes pixel values to [0, 1].
    Returns a float32 NumPy array of shape (size[1], size[0], 3).
    """
    # 1. Read image (OpenCV loads in BGR)
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Could not read image {img_path}")

    # 2. BGR → RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 3. Resize
    img = cv2.resize(img, size)

    # 4. Normalize to [0,1]
    img = img.astype("float32") / 255.0

    return img

def load_dataset(root_dir, size=(160, 160)):
    """
    Walks `root_dir`, expecting subfolders per label:
       root_dir/
         ├─ alice/
         │   ├─ alice_0001.jpg
         │   └─ …
         └─ bob/
             ├─ bob_0001.jpg
             └─ …
    Returns:
      X: NumPy array of shape (N, size[1], size[0], 3)
      y: Python list of string labels, length N
    """
    X, y = [], []
    for label in os.listdir(root_dir):
        class_dir = os.path.join(root_dir, label)
        if not os.path.isdir(class_dir):
            continue
        for fname in os.listdir(class_dir):
            if not fname.lower().endswith((".jpg", ".png")):
                continue
            path = os.path.join(class_dir, fname)
            img = preprocess_image(path, size=size)
            X.append(img)
            y.append(label)
    return np.array(X), y

# Example usage:
if __name__ == "__main__":
    data_dir = "data/known"            # your folder of subfolders per person
    proc_dir = "data/processed"        # where we'll save X and y
    # 1) Debug print
    print("Current working directory:", os.getcwd())
    # 2) Make sure the output folder exists
    os.makedirs(proc_dir, exist_ok=True)



    X, y = load_dataset(data_dir, size=(160,160))
    print(f"Loaded {len(X)} images for {len(set(y))} people.")
    print("Array shape:", X.shape)     # e.g. (1200, 160, 160, 3)

    # 1) Save as separate .npy files
    np.save(os.path.join(proc_dir, "X.npy"), X)
    np.save(os.path.join(proc_dir, "y.npy"), y)

    print(f"✅ Saved X and y into '{proc_dir}/' as X.npy, y.npy, and dataset.npz")