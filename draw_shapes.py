import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')

cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

cv2.circle(img, (300, 300), 50, (255, 0, 0), -1)

cv2.line(img, (0, 0), (500, 500), (0, 0, 255), 2)

cv2.imshow('Shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()