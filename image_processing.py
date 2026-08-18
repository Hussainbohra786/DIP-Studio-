import cv2
import numpy as np


# Grayscale
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# RGB to BGR
def rgb_to_bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


# BGR to RGB
def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Black and White
def black_white(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return bw


# Rotate 90 degree
def rotate(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


# Resize
def resize(img):
    return cv2.resize(img, (400, 400))


# Flip Horizontal
def flip_horizontal(img):
    return cv2.flip(img, 1)


# Flip Vertical
def flip_vertical(img):
    return cv2.flip(img, 0)


# Transpose
def transpose(img):
    return cv2.transpose(img)


# Average Blur
def blur(img):
    return cv2.blur(img, (7,7))


# Gaussian Blur
def gaussian_blur(img):
    return cv2.GaussianBlur(img,(7,7),0)


# Median Blur
def median_blur(img):
    return cv2.medianBlur(img,7)