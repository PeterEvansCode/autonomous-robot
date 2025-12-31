import cv2

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, frame = cap.read()
    if ret:
        print("Frame captured successfully.")
        cv2.imwrite("test_frame.jpg", frame)  # Save the captured frame
    else:
        print("Error: Cannot capture frame.")
    cap.release()
