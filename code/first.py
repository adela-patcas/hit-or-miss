import cv2
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7))
rows = 2
columns = 1

img = "img/nature.jpg"

InImgColor = cv2.imread(img)
InImgGray = cv2.imread(img, 0)
InImgRGB = cv2.cvtColor(InImgColor, cv2.COLOR_BGR2RGB)


fig.add_subplot(rows, columns, 1)
plt.imshow(InImgRGB)
plt.axis('off')
plt.title('The color input image')

fig.add_subplot(rows, columns, 2)
plt.imshow(InImgGray, cmap='gray')
plt.axis('off')
plt.title('The gray input image')
plt.show()
