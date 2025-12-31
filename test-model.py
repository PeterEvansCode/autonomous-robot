from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8 model (nano, small, medium, large, or custom path)
model = YOLO("yolov8n.pt")  # "n" = nano, smallest/faster, you can use "s", "m", "l" too

# --- Option 1: Run on an image ---
'''img = "test.jpg"  # path to your image
results = model(img)
results.show()  # opens the image with detected boxes'''

# --- Option 2: Run on webcam ---
cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  # detect objects
    annotated_frame = results[0].plot()  # draw boxes

    cv2.imshow("YOLOv8", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
