import numpy as np
from ximea import xiapi
import cv2

### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

#create instance for first connected camera
cam = xiapi.Camera()



#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
print('Opening first camerecho 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mba...')
cam.open_device()

#settings
cam.set_exposure(100000)
cam.set_param('imgdataformat','XI_RGB32')
cam.set_param('auto_wb', 1)
print('Exposure was set to %i us' %cam.get_exposure())

#create instance of Image to store image data and metadata
img = xiapi.Image()

#start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

k = 0
while k != 4:
    cam.get_image(img)
    frame = img.get_image_data_numpy()
    frame = cv2.resize(frame, (240,240))
    cv2.imshow("camera window", frame)
    if cv2.waitKey(1) == ord(" "):
        cam.get_image(img)
        image = img.get_image_data_numpy()
        image = cv2.resize(image,(240,240))
        cv2.imshow(f"img{str(k + 1)}", image)
        cv2.imwrite(f"img{str(k + 1)}.jpg", image)
        k += 1




# Remaining image processing stays the same
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
img3 = cv2.imread("img3.jpg")
img4 = cv2.imread("img4.jpg")
row1 = cv2.hconcat([img1, img2])
row2 = cv2.hconcat([img3, img4])
mozajka = cv2.vconcat([row1, row2]).astype(np.float32)
mozajka1 = np.clip(mozajka, 0, 255).astype(np.uint8)
cv2.imshow(f"M", mozajka1)
cv2.imwrite(f"M.jpg", mozajka1)
mt=mozajka.copy()


def saturated(sum_value):
    if sum_value > 255:
        sum_value = 255
    if sum_value < 0:
        sum_value = 0
    return sum_value


for j in range(1, 239):
    for i in range(1, 239):
        for k in range(0, 3):
            sum_value = (mt[j-1,i,k] + mt[j,i-1,k] - 4 * mt[j,i,k] + mt[j,i+1,k] + mt[j+1,i,k])
            mozajka[j, i, k] = saturated(sum_value)

mozajka = np.clip(mozajka, 0, 255).astype(np.uint8)


# Show and save the modified mosaic
cv2.imshow("M_2", mozajka)
cv2.imwrite("M_2.jpg", mozajka)

#otocenie
for i in range(0,240):
    for j in range(240,480):
        mozajka[j-240, 479-i] = mt[i,j]

cv2.imshow(f"M_3", mozajka)
cv2.imwrite(f"M_3.jpg", mozajka)
#otocenie

#RGB iba R
mozajka[240:480, 0:240, 0] = 0
mozajka[240:480, 0:240, 1] = 0

cv2.imshow(f"M_4", mozajka)
cv2.imwrite(f"M_4.jpg", mozajka)
#RGB iba R

#vypis
print(f"Data typ: {mozajka.dtype}")
print(f"Rozmery: {mozajka.shape}")
print(f"Velkost: {mozajka.size}")
#vypis

while cv2.waitKey(1) != ord('q'):
    pass

cv2.destroyAllWindows()

print('Stopping acquisition...')
print('Done.')
