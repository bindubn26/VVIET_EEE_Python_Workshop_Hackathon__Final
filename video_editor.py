import os

from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip,
    TextClip,
    concatenate_videoclips
)

from transitions import apply_transition
from effects import apply_effects


# -----------------------------------------
# Create Image Clips
# -----------------------------------------

def create_image_clips(
    image_paths,
    duration=3,
    size=(1280, 720)
):

    clips = []

    for image in image_paths:

        clip = (
            ImageClip(image)
            .resize(size)
            .set_duration(duration)
        )

        clips.append(clip)

    return clips


# -----------------------------------------
# Add Title
# -----------------------------------------

def add_title(
    video,
    title,
    duration=4
):

    txt = (
        TextClip(
            title,
            fontsize=60,
            color="white",
            font="Arial-Bold"
        )
        .set_duration(duration)
        .set_position(("center", "top"))
    )

    return CompositeVideoClip([video, txt])


# -----------------------------------------
# Add Subtitle
# -----------------------------------------

def add_subtitle(
    video,
    subtitle,
    duration=4
):

    txt = (
        TextClip(
            subtitle,
            fontsize=40,
            color="yellow",
            font="Arial"
        )
        .set_duration(duration)
        .set_position(("center", "bottom"))
    )

    return CompositeVideoClip([video, txt])


# -----------------------------------------
# Add Audio
# -----------------------------------------

def add_audio(
    video,
    voice_path=None,
    music_path=None
):

    audio_tracks = []

    if voice_path and os.path.exists(voice_path):
        audio_tracks.append(AudioFileClip(voice_path))

    if music_path and os.path.exists(music_path):
        music = AudioFileClip(music_path).volumex(0.35)
        audio_tracks.append(music)

    if audio_tracks:
        final_audio = CompositeAudioClip(audio_tracks)
        video = video.set_audio(final_audio)

    return video


# -----------------------------------------
# Build Video
# -----------------------------------------

def build_video(
    image_paths,
    title="Celebration",
    subtitle="Best Wishes",
    transition="Fade",
    effects=None,
    voice_path=None,
    music_path=None,
    duration=3
):

    clips = create_image_clips(
        image_paths,
        duration=duration
    )

    video = apply_transition(
        clips,
        transition
    )

    video = add_title(
        video,
        title
    )

    video = add_subtitle(
        video,
        subtitle
    )

    if effects:
        video = apply_effects(
            video,
            effects
        )

    video = add_audio(
        video,
        voice_path,
        music_path
    )

    return video


# -----------------------------------------
# Export Video
# -----------------------------------------

def export_video(
    video,
    output_path="outputs/final_video.mp4",
    fps=30
):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    video.write_videofile(
        output_path,
        fps=fps,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path


# -----------------------------------------
# Complete Pipeline
# -----------------------------------------

def create_celebration_video(
    image_paths,
    title,
    subtitle,
    transition,
    effects,
    voice_path=None,
    music_path=None,
    output_path="outputs/final_video.mp4"
):

    video = build_video(
        image_paths=image_paths,
        title=title,
        subtitle=subtitle,
        transition=transition,
        effects=effects,
        voice_path=voice_path,
        music_path=music_path
    )

    export_video(
        video,
        output_path
    )

    return output_path
