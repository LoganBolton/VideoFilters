import cv2
import numpy as np


def apply_rainbow_filter(frame):
    # Create a rainbow color gradient
    rainbow = np.zeros_like(frame, dtype=np.uint8)  # Specify the data type

    rows, cols, _ = frame.shape
    for r in range(rows):
        color = [int(255 * np.sin(np.pi * r / rows)),
                 int(255 * np.sin(np.pi * (r + rows) / rows)),
                 int(255 * np.sin(np.pi * (r + 2 * rows) / rows))]

        # Ensure color values are within the valid range (0-255)
        color = np.clip(color, 0, 255)

        rainbow[r, :, :] = color

    # Combine the original frame with the rainbow gradient
    rainbow_frame = cv2.addWeighted(frame, 0.7, rainbow, 0.3, 0)

    return rainbow_frame


# Open the MacBook camera
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    filtered_frame = apply_rainbow_filter(frame)

    cv2.imshow('Camera Filter', filtered_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
