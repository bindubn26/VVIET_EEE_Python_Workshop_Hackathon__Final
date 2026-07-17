import os

# ------------------------------------------
# PROJECT DIRECTORIES
# ------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
TEMP_DIR = os.path.join(BASE_DIR, "temp")

BACKGROUND_DIR = os.path.join(ASSETS_DIR, "backgrounds")
OVERLAY_DIR = os.path.join(ASSETS_DIR, "overlays")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
FONT_DIR = os.path.join(ASSETS_DIR, "fonts")

# ------------------------------------------
# SUPPORTED FILE TYPES
# ------------------------------------------

IMAGE_FORMATS = [
    "jpg",
    "jpeg",
    "png",
    "bmp",
    "webp"
]

AUDIO_FORMATS = [
    "mp3",
    "wav"
]

VIDEO_FORMATS = [
    "mp4",
    "mov",
    "avi",
    "webm"
]

# ------------------------------------------
# VIDEO SETTINGS
# ------------------------------------------

DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720

DEFAULT_RESOLUTION = (
    DEFAULT_WIDTH,
    DEFAULT_HEIGHT
)

DEFAULT_FPS = 30

DEFAULT_IMAGE_DURATION = 3

DEFAULT_TRANSITION = "Fade"

# ------------------------------------------
# AUDIO SETTINGS
# ------------------------------------------

DEFAULT_VOLUME = 0.5

DEFAULT_FADE_IN = 2

DEFAULT_FADE_OUT = 2

# ------------------------------------------
# AI SETTINGS
# ------------------------------------------

DEFAULT_LANGUAGE = "English"

DEFAULT_VOICE = "Female"

# ------------------------------------------
# EVENTS
# ------------------------------------------

SUPPORTED_EVENTS = [

    "Birthday",

    "Wedding Anniversary",

    "Graduation",

    "Baby Shower",

    "Achievement",

    "Father's Day",

    "Mother's Day",

    "Valentine's Day",

    "Christmas",

    "New Year",

    "Retirement",

    "Farewell",

    "Wedding Invitation",

    "Festival Greetings",

    "Custom"

]

# ------------------------------------------
# TRANSITIONS
# ------------------------------------------

TRANSITIONS = [

    "Fade",

    "Zoom",

    "Pan",

    "Ken Burns",

    "Cross Fade",

    "Rotate",

    "Slide Left",

    "Slide Right",

    "Blur"

]

# ------------------------------------------
# EFFECTS
# ------------------------------------------

CELEBRATION_EFFECTS = [

    "Confetti",

    "Balloons",

    "Fireworks",

    "Hearts",

    "Sparkles",

    "Cake",

    "Gift Boxes",

    "Party Lights",

    "Music Notes",

    "Stickers"

]

# ------------------------------------------
# EXPORT SETTINGS
# ------------------------------------------

EXPORT_FORMATS = [

    "MP4",

    "MOV",

    "AVI",

    "WEBM"

]

VIDEO_RESOLUTIONS = {

    "720p": (1280, 720),

    "1080p": (1920, 1080),

    "2K": (2560, 1440),

    "4K": (3840, 2160)

}

# ------------------------------------------
# CREATE REQUIRED FOLDERS
# ------------------------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

os.makedirs(TEMP_DIR, exist_ok=True)

os.makedirs(ASSETS_DIR, exist_ok=True)

os.makedirs(BACKGROUND_DIR, exist_ok=True)

os.makedirs(OVERLAY_DIR, exist_ok=True)

os.makedirs(MUSIC_DIR, exist_ok=True)

os.makedirs(FONT_DIR, exist_ok=True)
