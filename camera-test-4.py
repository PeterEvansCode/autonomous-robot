import cv2

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)

ret, frame = cap.read()
print("Frame captured successfully.")
cv2.imwrite("test_frame.jpg", frame)  # Save the captured frame

cap.release()
