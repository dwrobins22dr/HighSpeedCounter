import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Unable to open camera")

# Read frames from the camera
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame from camera")
        break

    # Display the captured frame
    cv2.imshow("Camera Test", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
