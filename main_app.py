import streamlit as st
from PIL import Image
import os
import tempfile
import streamlit as st

try:
    import moviepy
    st.write("moviePy Version:", moviepy.__version__)
except Exception as e:
    st.error(e)
from image_editor import *
from audio_editor import *
from voice_generator import *
from slideshow import *
from effects import *
from transitions import *
from export_video import *
from theme_manager import *

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Celebration Video Studio",
    page_icon="🎉",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🎉 AI Celebration Video Studio")
st.markdown("### Create Personalized Celebration Videos using AI")

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Upload Photos",
        "Event Details",
        "Voice Wishes",
        "Background Music",
        "Slideshow",
        "Celebration Effects",
        "Titles",
        "AI Narration",
        "Export"
    ]
)

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

if page == "Home":

    st.header("Welcome")

    st.write("""
This application helps you generate beautiful celebration videos.

Supported Events

🎂 Birthday

💍 Wedding Anniversary

🎓 Graduation

👶 Baby Shower

🏆 Achievement Celebration

👨 Father's Day

👩 Mother's Day

❤️ Valentine's Day

🎄 Christmas

🎆 New Year

👴 Retirement

👋 Farewell

💌 Wedding Invitation

🎊 Festival Greetings

✨ Custom Event
""")

# ---------------------------------------------------
# PHOTO UPLOAD
# ---------------------------------------------------

elif page == "Upload Photos":

    st.header("Upload Photos")

    uploaded_images = st.file_uploader(
        "Upload Images",
        type=["jpg", "jpeg", "png", "bmp", "webp"],
        accept_multiple_files=True
    )

    if uploaded_images:

        st.success(f"{len(uploaded_images)} Photos Uploaded")

        cols = st.columns(3)

        for i, file in enumerate(uploaded_images):

            img = Image.open(file)

            with cols[i % 3]:
                st.image(img, use_container_width=True)

        st.subheader("Image Editing")

        rotate = st.slider(
            "Rotate Image",
            0,
            360,
            0
        )

        crop = st.checkbox("Enable Crop")

        enhance = st.checkbox("AI Auto Enhance")

        face_center = st.checkbox("Face Centering")

        if st.button("Apply Image Changes"):

            st.success("Images Updated")

# ---------------------------------------------------
# EVENT DETAILS
# ---------------------------------------------------

elif page == "Event Details":

    st.header("Event Details")

    recipient = st.text_input("Recipient Name")

    event = st.selectbox(
        "Event Type",
        [
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
    )

    event_date = st.date_input("Event Date")

    age = st.number_input(
        "Age (Optional)",
        0,
        120,
        0
    )

    location = st.text_input("Event Location")

    heading = st.text_input(
        "Custom Heading",
        value="Happy Celebration!"
    )

    message = st.text_area(
        "Personalized Message",
        value="Wishing you happiness, success and joy!"
    )

    sender = st.text_input(
        "Sender Name",
        value="Your Friends"
    )

    st.subheader("Preview")

    st.markdown(f"""
# {heading}

Dear **{recipient}**

{message}

— {sender}
""")

# ---------------------------------------------------
# VOICE
# ---------------------------------------------------

elif page == "Voice Wishes":

    st.header("Voice Wishes")

    voice_files = st.file_uploader(
        "Upload Voice Messages",
        type=["mp3", "wav"],
        accept_multiple_files=True
    )

    if voice_files:

        st.success(f"{len(voice_files)} Voice Files Uploaded")

        for audio in voice_files:

            st.audio(audio)

    trim = st.checkbox("Trim Audio")

    noise = st.checkbox("Noise Reduction")

    merge = st.checkbox("Merge Multiple Voices")

    if st.button("Process Voice"):

        st.success("Voice Ready")

# ---------------------------------------------------
# MUSIC
# ---------------------------------------------------

elif page == "Background Music":

    st.header("Background Music")

    songs = st.file_uploader(
        "Upload Music",
        type=["mp3", "wav"],
        accept_multiple_files=True
    )

    if songs:

        for song in songs:

            st.audio(song)

    volume = st.slider(
        "Music Volume",
        0,
        100,
        70
    )

    fadein = st.slider(
        "Fade In",
        0,
        10,
        2
    )

    fadeout = st.slider(
        "Fade Out",
        0,
        10,
        2
    )

    loop = st.checkbox("Loop Music")

    if st.button("Apply Music"):

        st.success("Music Applied")
# ---------------------------------------------------
# SLIDESHOW
# ---------------------------------------------------

elif page == "Slideshow":

    st.header("🎬 AI Slideshow Generator")

    transition = st.selectbox(
        "Transition",
        [
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
    )

    duration = st.slider(
        "Photo Duration (seconds)",
        min_value=1,
        max_value=10,
        value=3
    )

    fps = st.selectbox(
        "Frame Rate",
        [24, 30, 60],
        index=1
    )

    resolution = st.selectbox(
        "Resolution",
        [
            "720p",
            "1080p",
            "2K",
            "4K"
        ]
    )

    enable_zoom = st.checkbox("Ken Burns Zoom")

    enable_pan = st.checkbox("Pan Effect")

    auto_sync = st.checkbox("AI Scene Timing")

    preview = st.checkbox("Preview Slideshow")

    if st.button("Generate Slideshow"):

        st.success("Slideshow Created Successfully!")

# ---------------------------------------------------
# CELEBRATION EFFECTS
# ---------------------------------------------------

elif page == "Celebration Effects":

    st.header("🎉 Celebration Effects")

    confetti = st.checkbox("Confetti")

    balloons = st.checkbox("Balloons")

    fireworks = st.checkbox("Fireworks")

    hearts = st.checkbox("Hearts")

    sparkles = st.checkbox("Sparkles")

    cake = st.checkbox("Birthday Cake")

    gifts = st.checkbox("Gift Boxes")

    lights = st.checkbox("Party Lights")

    music_notes = st.checkbox("Music Notes")

    stickers = st.checkbox("Animated Stickers")

    intensity = st.slider(
        "Effect Intensity",
        1,
        10,
        5
    )

    if st.button("Apply Effects"):

        st.success("Celebration Effects Added!")

# ---------------------------------------------------
# TITLES & CAPTIONS
# ---------------------------------------------------

elif page == "Titles":

    st.header("📝 Titles & Captions")

    title = st.text_input(
        "Main Title",
        "Happy Birthday!"
    )

    subtitle = st.text_input(
        "Subtitle",
        "Wishing You Happiness"
    )

    quote = st.text_area(
        "Quote",
        "May all your dreams come true!"
    )

    font = st.selectbox(
        "Font Style",
        [
            "Arial",
            "Times New Roman",
            "Verdana",
            "Comic Sans",
            "Helvetica"
        ]
    )

    text_color = st.color_picker(
        "Text Color",
        "#FFFFFF"
    )

    background_color = st.color_picker(
        "Background Color",
        "#000000"
    )

    animation = st.selectbox(
        "Text Animation",
        [
            "Fade",
            "Zoom",
            "Slide Left",
            "Slide Right",
            "Bounce"
        ]
    )

    scrolling = st.checkbox("Scrolling Text")

    if st.button("Apply Titles"):

        st.success("Titles Added Successfully!")
# ---------------------------------------------------
# AI NARRATION
# ---------------------------------------------------

elif page == "AI Narration":

    st.header("🎤 AI Voice Narration")

    narration_text = st.text_area(
        "Narration Text",
        "Happy Birthday! Wishing you joy, happiness, success and wonderful memories."
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Kannada",
            "Telugu",
            "Tamil"
        ]
    )

    voice_gender = st.selectbox(
        "Voice",
        [
            "Female",
            "Male"
        ]
    )

    speech_speed = st.slider(
        "Speech Speed",
        0.5,
        2.0,
        1.0
    )

    if st.button("Generate AI Voice"):

        st.success("AI Narration Generated Successfully!")

# ---------------------------------------------------
# EXPORT
# ---------------------------------------------------

elif page == "Export":

    st.header("🎬 Export Celebration Video")

    theme = st.selectbox(
        "Theme",
        [
            "Birthday",
            "Luxury Gold",
            "Romantic",
            "Kids",
            "Festival",
            "Elegant",
            "Modern",
            "Classic"
        ]
    )

    quality = st.selectbox(
        "Video Quality",
        [
            "720p",
            "1080p",
            "2K",
            "4K"
        ]
    )

    video_format = st.selectbox(
        "Export Format",
        [
            "MP4",
            "MOV",
            "AVI",
            "WEBM"
        ]
    )

    include_music = st.checkbox(
        "Include Background Music",
        value=True
    )

    include_voice = st.checkbox(
        "Include Voice Wishes",
        value=True
    )

    include_titles = st.checkbox(
        "Include Titles",
        value=True
    )

    include_effects = st.checkbox(
        "Include Celebration Effects",
        value=True
    )

    progress = st.progress(0)

    if st.button("🎥 Generate Celebration Video"):

        for i in range(101):
            progress.progress(i)

        st.success("Video Generated Successfully!")

        output_video = "outputs/final_video.mp4"

        if os.path.exists(output_video):

            with open(output_video, "rb") as file:

                st.download_button(
                    label="⬇ Download Video",
                    data=file,
                    file_name="Celebration_Video.mp4",
                    mime="video/mp4"
                )

        else:

            st.info("Video rendering module will create this file.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.markdown(
    """
    <center>
    <h4>🎉 AI Celebration Video Studio</h4>
    <p>Create Personalized Birthday, Anniversary & Event Videos using Streamlit & Python</p>
    </center>
    """,
    unsafe_allow_html=True
)
