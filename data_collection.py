import cv2
import os

cap = cv2.VideoCapture(0)
sign = "A"  # Specify the current sign being recorded
output_dir = f"data/{sign}"
os.makedirs(output_dir, exist_ok=True)

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)

    # Save frame to the directory
    cv2.imwrite(f"{output_dir}/{count}.jpg", frame)
    count += 1

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
