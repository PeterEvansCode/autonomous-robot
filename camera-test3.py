import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Ensure V4L2 backend

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, frame = cap.read()
    if ret:
        print("Frame captured successfully.")
        cv2.imwrite("test_frame.jpg", frame)  # Save the frame as test_frame.jpg
    else:
        print("Error: Cannot capture frame.")

cap.release()
