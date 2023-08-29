import cv2
import numpy as np


def apply_rainbow_filter(frame):
    # Create a rainbow color gradient
    rainbow = np.zeros_like(frame)
    rows, cols, _ = frame.shape
    for r in range(rows):
        color = [int(255 * np.sin(np.pi * r / rows)),
                 int(255 * np.sin(np.pi * (r + rows) / rows)),
                 int(255 * np.sin(np.pi * (r + 2 * rows) / rows))]
        rainbow[r, :, :] = color

    # Combine the original frame with the rainbow gradient
    rainbow_frame = cv2.addWeighted(frame, 0.7, rainbow, 0.3, 0)

    return rainbow_frame


cap = cv2.VideoCapture('/Users/Everlie/Documents/GitHub/VideoFilters/demo.mp4')

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_rainbow_video.mp4', fourcc,
                      fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rainbow_frame = apply_rainbow_filter(frame)

    out.write(rainbow_frame)

    cv2.imshow('Rainbow Video', rainbow_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
