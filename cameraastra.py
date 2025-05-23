# camera_test.py

import cv2

def test_camera(camera_index=2):
    """
    Opens the camera, displays the live feed, and allows you to
    press 'c' to capture a frame or 'q' to quit.

    :param camera_index: index of the camera (0 for default webcam)
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Cannot open camera index {camera_index}")
        return

    print("Press 'c' to capture a frame, 'q' to quit.")
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Show the live video
        cv2.imshow("Camera Test", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            # Save a captured frame
            filename = f"capture_{frame_count:03d}.png"
            cv2.imwrite(filename, frame)
            print(f"Captured frame saved as {filename}")
            frame_count += 1
        elif key == ord('q'):
            # Quit the loop
            print("Quitting camera test.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera()
