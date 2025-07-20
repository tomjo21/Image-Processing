import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/flower.jpg', cv2.IMREAD_GRAYSCALE)

roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

roberts_x_img = cv2.filter2D(img, cv2.CV_64F, roberts_x)
roberts_y_img = cv2.filter2D(img, cv2.CV_64F, roberts_y)

roberts_combined = cv2.magnitude(roberts_x_img, roberts_y_img)
roberts_combined = np.uint8(255 * roberts_combined / np.max(roberts_combined))

plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(1, 4, 2), plt.imshow(roberts_x_img, cmap='gray')
plt.title('Roberts X'), plt.axis('off')

plt.subplot(1, 4, 3), plt.imshow(roberts_y_img, cmap='gray')
plt.title('Roberts Y'), plt.axis('off')

plt.subplot(1, 4, 4), plt.imshow(roberts_combined, cmap='gray')
plt.title('Roberts Combined'), plt.axis('off')

plt.show()
