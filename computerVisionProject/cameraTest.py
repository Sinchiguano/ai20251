import cv2

def test_camera(camera_index=0):
    """
    Open the webcam at `camera_index`, display each frame in a window,
    and quit when you press 'q'.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"❌ Unable to open camera #{camera_index}")
        return

    print(f"✅ Camera #{camera_index} opened. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Frame capture failed; exiting.")
            break

        # Show the live frame
        cv2.imshow("Camera Test", frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Change the index if you have multiple cameras (0, 1, 2, ...)
    test_camera(camera_index=2)
