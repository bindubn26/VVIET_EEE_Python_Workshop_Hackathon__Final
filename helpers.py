import os
from PIL import Image

from image_editor import prepare_slideshow_image
from slideshow import export_slideshow
from voice_generator import generate_ai_voice
from audio_editor import prepare_audio
from video_editor import create_celebration_video


# -------------------------------------------------
# Save Uploaded Images
# -------------------------------------------------

def save_uploaded_images(uploaded_files, folder="temp"):

    os.makedirs(folder, exist_ok=True)

    image_paths = []

    for file in uploaded_files:

        image = Image.open(file).convert("RGB")

        image = prepare_slideshow_image(image)

        filename = os.path.join(folder, file.name)

        image.save(filename)

        image_paths.append(filename)

    return image_paths


# -------------------------------------------------
# Save Uploaded Music
# -------------------------------------------------

def save_uploaded_music(uploaded_music, folder="temp"):

    if uploaded_music is None:
        return None

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, uploaded_music.name)

    with open(filepath, "wb") as f:
        f.write(uploaded_music.read())

    return filepath


# -------------------------------------------------
# Save Uploaded Voice
# -------------------------------------------------

def save_uploaded_voice(uploaded_voice, folder="temp"):

    if uploaded_voice is None:
        return None

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, uploaded_voice.name)

    with open(filepath, "wb") as f:
        f.write(uploaded_voice.read())

    return filepath


# -------------------------------------------------
# Generate AI Voice
# -------------------------------------------------

def create_ai_voice(
    message,
    language="English"
):

    return generate_ai_voice(
        text=message,
        language=language,
        output_path="temp/ai_voice.mp3"
    )


# -------------------------------------------------
# Prepare Final Audio
# -------------------------------------------------

def create_final_audio(
    voice_path=None,
    music_path=None
):

    return prepare_audio(
        voice_path=voice_path,
        music_path=music_path,
        output_path="temp/final_audio.mp3"
    )


# -------------------------------------------------
# Generate Slideshow
# -------------------------------------------------

def create_photo_slideshow(
    image_paths,
    animation="Fade"
):

    return export_slideshow(
        image_paths=image_paths,
        output_path="temp/slideshow.mp4",
        duration=3,
        animation=animation
    )


# -------------------------------------------------
# Generate Celebration Video
# -------------------------------------------------

def generate_video(
    image_paths,
    title,
    subtitle,
    transition,
    effects,
    voice_path=None,
    music_path=None
):

    return create_celebration_video(
        image_paths=image_paths,
        title=title,
        subtitle=subtitle,
        transition=transition,
        effects=effects,
        voice_path=voice_path,
        music_path=music_path,
        output_path="outputs/final_video.mp4"
    )


# -------------------------------------------------
# Clean Temporary Files
# -------------------------------------------------

def clean_temp(folder="temp"):

    if not os.path.exists(folder):
        return

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        try:
            os.remove(path)
        except:
            pass
