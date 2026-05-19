# 🚀 OpenCV Image Resize Project

<div align="center">

# 🖼️ OpenCV Image Resizer

✨ Resize Images Easily Using Python & OpenCV ✨

</div>

---

# 📂 Project Structure

```bash
OpenCV_/
│
├── resize_image.py
│
├── images/
│   └── sample.jpg
│
└── resized_output.jpg
```

---

# 🎯 About Project

This project demonstrates how to:

✅ Read an image using OpenCV  
✅ Resize image dimensions  
✅ Display image on screen  
✅ Save resized image automatically  

Perfect for beginners learning Python Computer Vision 👨‍💻

---

# ⚙️ Installation

Install OpenCV library:

```bash
pip install opencv-python
```

---

# ▶️ Run The Project

Open terminal inside project folder and run:

```bash
python resize_image.py
```

---

# 🧠 Python Code

```python
import cv2

# Load image
image = cv2.imread("images/sample.jpg")

# Check image loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image
resized_image = cv2.resize(image, (500, 500))

# Show original image
cv2.imshow("Original Image", image)

# Show resized image
cv2.imshow("Resized Image", resized_image)

# Save resized image
cv2.imwrite("resized_output.jpg", resized_image)

print("✅ Image resized successfully!")
print("💾 Saved as resized_output.jpg")

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
```

---

# 🌟 Features

✨ Beginner Friendly  
✨ Fast Image Processing  
✨ Simple Python Code  
✨ Real-Time Image Display  
✨ Auto Save Output Image  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 🐍 | Programming Language |
| OpenCV 👁️ | Image Processing |

---

# 📸 Output

After running the project:

✅ Original image window opens  
✅ Resized image window opens  
✅ Output image saved automatically  

---

# 🔥 Future Improvements

- Add image rotation
- Add grayscale conversion
- Add blur effects
- Add GUI using Tkinter
- Add live webcam resizing

---

<div align="center">

## ⭐ If you like this project, give it a star ⭐

Made with ❤️ by Omkar Sathe

</div>
