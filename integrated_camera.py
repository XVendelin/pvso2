import numpy as np
import cv2 as cv


def nothing(x):
    pass


# Open the default camera (0 for the first webcam)
cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set camera properties (adjust as needed)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Create a window for trackbars
cv.namedWindow('img')

# Create trackbars
cv.createTrackbar('param1', 'img', 50, 100, nothing)
cv.createTrackbar('param2', 'img', 50, 100, nothing)
cv.createTrackbar('radius_min', 'img', 1, 100, nothing)
cv.createTrackbar('radius_max', 'img', 100, 100, nothing)
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'img', 1, 1, nothing)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize for display
    frame = cv.resize(frame, (640, 480))

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    # Read trackbar positions
    p1 = cv.getTrackbarPos('param1', 'img')
    p2 = cv.getTrackbarPos('param2', 'img')
    rmin = cv.getTrackbarPos('radius_min', 'img')
    rmax = cv.getTrackbarPos('radius_max', 'img')
    s = cv.getTrackbarPos(switch, 'img')

    # Create a copy for output
    output = frame.copy()

    if s == 1:
        # Detect circles
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=rmin, maxRadius=rmax)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Draw outer circle
                cv.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)  # Draw center

    # Show the processed frame
    cv.imshow('img', output)

    # Exit if 'space' is pressed
    if cv.waitKey(1) & 0xFF == ord(' '):
        break

# Release the camera and close windows
cam.release()
cv.destroyAllWindows()
