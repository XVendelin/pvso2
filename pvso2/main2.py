import numpy as np
from ximea import xiapi
import cv2 as cv


def nothing(x):
    pass


# Create camera instance
cam = xiapi.Camera()

# Open the first connected camera
print('Opening first camera...')
cam.open_device()

# Camera settings
cam.set_exposure(100000)
cam.set_param('imgdataformat', 'XI_RGB32')
cam.set_param('auto_wb', 1)
print(f'Exposure set to {cam.get_exposure()} us')

# Create instance of Image to store image data
img = xiapi.Image()

# Start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

# Create a window for trackbars
cv.namedWindow('img')

# Create trackbars (only once)
cv.createTrackbar('param1', 'img', 50, 100, nothing)
cv.createTrackbar('param2', 'img', 30, 100, nothing)
cv.createTrackbar('radius', 'img', 1, 100, nothing)
cv.createTrackbar('radius_max', 'img', 100, 100, nothing)

switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'img', 1, 1, nothing)

# Continuous processing loop
while True:
    # Get image from camera
    cam.get_image(img)
    frame = img.get_image_data_numpy()

    # Resize for display
    frame = cv.resize(frame, (640, 480))

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    # Read trackbar positions
    p1 = cv.getTrackbarPos('param1', 'img')
    p2 = cv.getTrackbarPos('param2', 'img')
    r = cv.getTrackbarPos('radius', 'img')
    rmax = cv.getTrackbarPos('radius_max', 'img')
    s = cv.getTrackbarPos(switch, 'img')

    # Create a copy of the frame for drawing circles
    output = frame.copy()

    if s == 1:
        # Detect circles using trackbar parameters
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=r, maxRadius=rmax)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                x, y, radius = i
                cv.circle(output, (x, y), radius, (0, 255, 0), 2)  # Draw outer circle
                cv.circle(output, (x, y), 2, (0, 0, 255), 3)  # Draw center

                # Display the radius as text near the detected circle
                cv.putText(output, f'r: {radius}', (x - 20, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show the processed frame
    cv.imshow('img', output)

    # Exit if 'space' is pressed
    if cv.waitKey(1) & 0xFF == ord(' '):
        break

# Stop camera acquisition and close windows
cam.stop_acquisition()
cam.close_device()
cv.destroyAllWindows()
