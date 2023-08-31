import cv2
import numpy as np

def apply_rainbow_effect(frame):
    # Convert frame to float32 to prevent overflow
    frame = np.float32(frame)

    # Get height and width of the frame
    h, w, _ = frame.shape

    # Create an array of indices
    x = np.linspace(-2*np.pi, 2*np.pi, w)
    y = np.linspace(-2*np.pi, 2*np.pi, h).reshape(-1, 1)

    # Create sinusoidal functions to create the rainbow effect
    r_effect = np.sin(y + x) * 45
    g_effect = np.sin(y + x + 2*np.pi/3) * 45
    b_effect = np.sin(y + x + 4*np.pi/3) * 45

    # Add the effects to the original frame values
    frame[..., 0] += b_effect
    frame[..., 1] += g_effect
    frame[..., 2] += r_effect

    # Clip values to ensure they are within [0, 255]
    frame = np.clip(frame, 0, 255)

    return frame.astype(np.uint8)

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Apply the rainbow effect
    rainbow_frame = apply_rainbow_effect(frame)

    # Show the output
    cv2.imshow('Rainbow Effect', rainbow_frame)

    # Break loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
