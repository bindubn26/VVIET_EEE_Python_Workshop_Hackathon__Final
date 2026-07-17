from PIL import Image, ImageEnhance, ImageOps
import cv2
import numpy as np


def load_image(file):
    """Load uploaded image."""
    return Image.open(file).convert("RGB")


def rotate_image(image, angle):
    """Rotate image."""
    return image.rotate(angle, expand=True)


def crop_center(image, crop_width, crop_height):
    """Crop image from center."""
    width, height = image.size

    left = max((width - crop_width) // 2, 0)
    top = max((height - crop_height) // 2, 0)
    right = min(left + crop_width, width)
    bottom = min(top + crop_height, height)

    return image.crop((left, top, right, bottom))


def resize_image(image, size=(1280, 720)):
    """Resize image."""
    return image.resize(size)


def auto_enhance(image):
    """Automatically enhance brightness, contrast and sharpness."""

    image = ImageEnhance.Brightness(image).enhance(1.05)
    image = ImageEnhance.Contrast(image).enhance(1.15)
    image = ImageEnhance.Color(image).enhance(1.15)
    image = ImageEnhance.Sharpness(image).enhance(1.2)

    return image


def grayscale(image):
    """Convert image to grayscale."""
    return ImageOps.grayscale(image)


def flip_horizontal(image):
    """Flip image horizontally."""
    return ImageOps.mirror(image)


def flip_vertical(image):
    """Flip image vertically."""
    return ImageOps.flip(image)


def detect_face(image):
    """
    Detect the largest face.
    Returns (x, y, w, h) or None.
    """

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    if len(faces) == 0:
        return None

    largest = max(faces, key=lambda f: f[2] * f[3])

    return largest


def face_center_crop(image):
    """
    Crop image around detected face.
    """

    face = detect_face(image)

    if face is None:
        return image

    x, y, w, h = face

    img = np.array(image)

    height, width = img.shape[:2]

    cx = x + w // 2
    cy = y + h // 2

    crop_w = min(width, 700)
    crop_h = min(height, 700)

    left = max(cx - crop_w // 2, 0)
    top = max(cy - crop_h // 2, 0)

    right = min(left + crop_w, width)
    bottom = min(top + crop_h, height)

    cropped = img[top:bottom, left:right]

    return Image.fromarray(cropped)


def prepare_slideshow_image(image):
    """
    Complete preprocessing for slideshow.
    """

    image = auto_enhance(image)
    image = face_center_crop(image)
    image = resize_image(image)

    return image
