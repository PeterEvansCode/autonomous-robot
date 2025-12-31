import cv2

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

# Set a lower resolution (640x480 is a good starting point)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, frame = cap.read()
    if ret:
        print("Frame captured successfully.")
        cv2.imwrite("test_frame.jpg", frame)
    else:
        print("Error: Cannot capture frame.")
    cap.release()
