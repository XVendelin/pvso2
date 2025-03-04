import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Load the image
img = cv.imread('img.jpg')
assert img is not None, "File could not be read, check with os.path.exists()"

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

# Create a window
cv.namedWindow('img')

# Create trackbars
cv.createTrackbar('param1', 'img', 50, 100, nothing)
cv.createTrackbar('param2', 'img', 30, 100, nothing)
cv.createTrackbar('radius', 'img', 1, 100, nothing)

switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'img', 1, 1, nothing)

while True:
    # Get trackbar positions
    p1 = cv.getTrackbarPos('param1', 'img')
    p2 = cv.getTrackbarPos('param2', 'img')
    r = cv.getTrackbarPos('radius', 'img')
    s = cv.getTrackbarPos(switch, 'img')

    # Copy original image to avoid overwriting
    output = img.copy()

    if s == 1:
        # Detect circles using updated parameters
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=r, maxRadius=100)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Show the image with updated circles
    cv.imshow('img', output)

    # Exit on pressing 'Esc'
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
