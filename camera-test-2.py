import cv2
cap = cv2.VideoCapture(0)  # Use the correct video device index (0, 1, etc.)

ret, frame = cap.read()
if ret:
    cv2.imwrite("test_frame.jpg", frame)  # Save a frame to confirm capture
else:
    print("Error: Cannot capture frame")
cap.release()
