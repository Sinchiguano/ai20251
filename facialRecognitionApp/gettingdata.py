# import cv2
# import os
# import time
# import argparse

# def record_video(output_dir, subject_name, camera_index=0, fps=20.0, width=640, height=480):
#     # Ensure output directory exists
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Build output filename
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     filename = f"{subject_name}_{timestamp}.avi"
#     filepath = os.path.join(output_dir, filename)
    
#     # Open the webcam
#     cap = cv2.VideoCapture(camera_index)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'MJPG', 'MP4V'
#     out = cv2.VideoWriter(filepath, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
    
#     if not cap.isOpened():
#         print(f"❌ Cannot open camera index {camera_index}")
#         return
    
#     print(f"🔴 Recording to {filepath}. Press 'q' to stop.")
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("⚠️  Frame grab failed, exiting.")
#             break
        
#         # Write the frame
#         out.write(frame)
        
#         # Display live feed
#         cv2.imshow("Recording (press 'q' to stop)", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Cleanup
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     print("✅ Recording stopped and file saved.")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Record webcam video for face-data collection"
#     )
#     parser.add_argument("output_dir", help="Directory to store recordings")
#     parser.add_argument("subject_name", help="Label for this recording (e.g. person's name)")
#     parser.add_argument("--camera", type=int, default=0, help="Camera index (default 0)")
#     parser.add_argument("--fps", type=float, default=20.0, help="Frames per second")
#     parser.add_argument("--width", type=int, default=640, help="Frame width")
#     parser.add_argument("--height", type=int, default=480, help="Frame height")
    
#     args = parser.parse_args()
#     record_video(
#         args.output_dir,
#         args.subject_name,
#         camera_index=args.camera,
#         fps=args.fps,
#         width=args.width,
#         height=args.height
#     )


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
