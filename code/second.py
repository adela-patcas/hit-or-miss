import cv2
import matplotlib.pyplot as plt
import math

InImg = cv2.imread("img/binary.png", 0)  # importing binary image
OutImg = InImg * 0
dimensions = InImg.shape  # dimensions of the image
height = dimensions[0]
width = dimensions[1]

for row in range(1, height-1):
    for col in range(1, width-1):
        if InImg[row, col] > 200:
            InImg[row, col] = 255
        else:
            InImg[row, col] = 0
plt.figure()
plt.imshow(InImg, cmap="gray")  # showing the input image
plt.show()

top_right_corner = [[0, -1, 0], [1, 1, -1], [0, 1, 0]]
top_left_corner = [[0, -1, 0], [-1, 1, 1], [0, 1, 0]]
bottom_left_corner = [[0, 1, 0], [-1, 1, 1], [0, -1, 0]]
bottom_right_corner = [[0, 1, 0], [1, 1, -1], [0, -1, 0]]

plt.figure()
plt.imshow(top_right_corner, cmap="gray")
plt.figure()
plt.imshow(top_left_corner, cmap="gray")
plt.figure()
plt.imshow(bottom_left_corner, cmap="gray")
plt.figure()
plt.imshow(bottom_right_corner, cmap="gray")
plt.show()

dimensions = InImg.shape  # dimensions of the image
height = dimensions[0]
width = dimensions[1]

for row in range(1, height-1):
    for col in range(1, width-1):
        local_pixels = InImg[row-1:row+2, col-1:col+2]
        filtered_pixels_tr = top_right_corner*local_pixels
        filtered_pixels_tl = top_left_corner*local_pixels
        filtered_pixels_bl = bottom_left_corner*local_pixels
        filtered_pixels_br = bottom_right_corner*local_pixels
        # Math.trunc truncates the value, the result is an integer, with anything after the decimal being discarded
        pixel_tr = math.trunc((filtered_pixels_tr.sum() + 2 * 255)/(5*255))
        # Without the truncate function, random values may appear within the pixels and the image will
        pixel_tl = math.trunc((filtered_pixels_tl.sum() + 2 * 255)/(5*255))
        # be "corrupted" with unwanted values
        pixel_bl = math.trunc((filtered_pixels_bl.sum() + 2 * 255)/(5*255))
        pixel_br = math.trunc((filtered_pixels_br.sum() + 2 * 255)/(5*255))
        OutImg[row, col] = pixel_tr + pixel_tl + pixel_bl + pixel_br
plt.figure(figsize=(10, 10))
plt.imshow(OutImg, cmap="gray")
plt.show()
