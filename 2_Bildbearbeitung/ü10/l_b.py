import cv2
import numpy as np

img = cv2.imread("../../data/car.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500, 500))
# Do some preprocessing
img = img.astype(float)
img = 50 + (105 * img / 255)
cv2.imshow("Original", img.astype(np.uint8))

# Implement CLAHE
new_image = np.zeros_like(img)
height, width = img.shape
for x in range(width):
    for y in range(height):
        x1, x2 = np.maximum(0, x - 25), np.minimum(x + 25, height)
        y1, y2 = np.maximum(0, y - 25), np.minimum(y + 25, height)
        hist, values = np.histogram(img[y1:y2, x1:x2], bins=256, range=(0, 256))
        clip_limit = 0.6 * round(np.max(hist))
        higher_values = hist >= clip_limit
        sum_of_higher_values = np.sum(hist[higher_values] - clip_limit)
        hist = np.minimum(hist, clip_limit)
        hist = hist + round(sum_of_higher_values / 256)
        cum_hist = np.cumsum(hist)
        v = round(img[y, x])
        new_image[y, x] = v * cum_hist[v] / cum_hist[255]

cv2.imshow("CLAHE", new_image.astype(np.uint8))

cv2.waitKey(0)

