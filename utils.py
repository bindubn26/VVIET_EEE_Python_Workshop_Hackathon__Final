import os
import uuid
from PIL import Image


def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def generate_filename(extension):
    """
    Generate a unique filename.
    """
    return f"{uuid.uuid4().hex}.{extension}"


def save_uploaded_image(uploaded_file, folder="temp"):
    """
    Save a Streamlit uploaded image.
    """
    ensure_directory(folder)

    ext = uploaded_file.name.split(".")[-1]
    filename = generate_filename(ext)

    filepath = os.path.join(folder, filename)

    image = Image.open(uploaded_file)
    image.save(filepath)

    return filepath


def save_uploaded_audio(uploaded_file, folder="temp"):
    """
    Save a Streamlit uploaded audio file.
    """
    ensure_directory(folder)

    ext = uploaded_file.name.split(".")[-1]
    filename = generate_filename(ext)

    filepath = os.path.join(folder, filename)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    return filepath


def clean_temp(folder="temp"):
    """
    Delete all files in the temporary folder.
    """
    if not os.path.exists(folder):
        return

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            os.remove(path)
