import cv2

# Read image
img = cv2.imread('images/sample.jpg')

# Resize image
resized = cv2.resize(img, (300, 300))

# Show resized image
cv2.imshow('Resized Image', resized)

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()