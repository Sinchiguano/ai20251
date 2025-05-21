import cv2
import os
import time
import argparse

def record_video(output_dir, subject_name, camera_index=0, fps=20.0, width=640, height=480):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Build output filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{subject_name}_{timestamp}.avi"
    filepath = os.path.join(output_dir, filename)
    
    # Open the webcam
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'MJPG', 'MP4V'
    out = cv2.VideoWriter(filepath, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
    
    if not cap.isOpened():
        print(f"❌ Cannot open camera index {camera_index}")
        return
    
    print(f"🔴 Recording to {filepath}. Press 'q' to stop.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️  Frame grab failed, exiting.")
            break
        
        # Write the frame
        out.write(frame)
        
        # Display live feed
        cv2.imshow("Recording (press 'q' to stop)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("✅ Recording stopped and file saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Record webcam video for face-data collection"
    )
    parser.add_argument("output_dir", help="Directory to store recordings")
    parser.add_argument("subject_name", help="Label for this recording (e.g. person's name)")
    parser.add_argument("--camera", type=int, default=0, help="Camera index (default 0)")
    parser.add_argument("--fps", type=float, default=20.0, help="Frames per second")
    parser.add_argument("--width", type=int, default=640, help="Frame width")
    parser.add_argument("--height", type=int, default=480, help="Frame height")
    
    args = parser.parse_args()
    record_video(
        args.output_dir,
        args.subject_name,
        camera_index=args.camera,
        fps=args.fps,
        width=args.width,
        height=args.height
    )
