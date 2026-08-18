
# 📷 DIP Studio Pro

A web-based **Digital Image Processing (DIP)** application developed using **PHP, Python, OpenCV, HTML, CSS, and JavaScript**. The application allows users to upload images and perform various image processing operations through an interactive and user-friendly interface.

---
<img width="1887" height="884" alt="Screenshot 2026-08-18 151742" src="https://github.com/user-attachments/assets/924c1c67-cc32-4349-8196-8b1c048904ba" />
<img width="1877" height="886" alt="Screenshot 2026-08-18 151830" src="https://github.com/user-attachments/assets/78990eee-c2c6-4f68-b077-d458f5c96a61" />
<img width="1894" height="880" alt="Screenshot 2026-08-18 151901" src="https://github.com/user-attachments/assets/b5439407-dcba-4df5-8e33-b1fa6d6ce892" />
<img width="1919" height="892" alt="Screenshot 2026-08-18 151926" src="https://github.com/user-attachments/assets/4e19457c-c95d-4226-9a60-02da8f6122a6" />



## 🚀 Features

- 📤 Upload images (JPG, JPEG, PNG, BMP, TIFF, WEBP)
- 🎨 Convert image to Grayscale
- ⚫ Black & White (Binary) Conversion
- 🔄 Rotate Image
- ↔️ Flip Image
- 🔁 Transpose Image
- 📏 Resize Image
- 🌫️ Blur Filter
- ✨ Gaussian Blur
- 🧹 Median Blur
- 📊 Histogram Visualization
- 🌈 Color Model Visualization
  - RGB
  - HSV
  - LAB
  - YCrCb
- 💾 Download Processed Images

---

## 🛠️ Technologies Used

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript

- **Backend**
  - PHP

- **Image Processing**
  - Python
  - OpenCV
  - NumPy
  - Matplotlib

- **Local Server**
  - XAMPP (Apache)

---

## 📂 Project Structure

```
DIP-Studio-Pro/
│
├── assets/
│   ├── style.css
│   └── script.js
│
├── python/
│   └── processor.py
│
├── uploads/
│
├── outputs/
│
├── index.php
├── upload.php
├── process.php
├── download.php
├── color_model.php
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DIP-Studio-Pro.git
```

### 2. Move the Project

Copy the project folder into the **htdocs** directory of XAMPP.

Example:

```
C:\xampp\htdocs\DIP-Studio-Pro
```

### 3. Install Python Packages

```bash
pip install opencv-python numpy matplotlib
```

### 4. Start XAMPP

- Start **Apache**
- Open your browser

```
http://localhost/DIP-Studio-Pro
```

---

## 🖥️ How It Works

1. Upload an image.
2. Select any image processing operation.
3. PHP sends the image path and selected operation to Python.
4. OpenCV processes the image.
5. The processed image is displayed instantly.
6. Download the processed image.

---

## 📷 Supported Image Formats

- JPG
- JPEG
- PNG
- BMP
- TIFF
- WEBP

---

## 📸 Available Operations

### Color Operations

- Grayscale
- RGB ↔ BGR Conversion
- Black & White (Binary)

### Image Transformations

- Resize
- Rotate
- Flip
- Transpose

### Filters

- Blur
- Gaussian Blur
- Median Blur

### Analysis

- Histogram

### Color Models

- RGB
- HSV
- LAB
- YCrCb

---

## 🔮 Future Improvements

- Edge Detection (Sobel, Canny)
- Image Sharpening
- Morphological Operations
- Face Detection
- Object Detection
- OCR (Optical Character Recognition)
- AI-Based Image Enhancement
- Real-Time Webcam Processing
- Cloud Deployment

---

## 🎯 Learning Outcomes

Through this project, we learned:

- Digital Image Processing fundamentals
- OpenCV image manipulation
- PHP and Python integration
- File handling using PHP
- Web application development
- Color space conversions
- Histogram analysis
- Image filtering techniques

---

## 👨‍💻 Developed By

**Hussain Bohra**  
B.Tech Computer Science Engineering

---

## 📜 License

This project is developed for **academic and educational purposes**.
