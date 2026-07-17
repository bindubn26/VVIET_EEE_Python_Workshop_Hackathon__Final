from moviepy.editor import (
    ImageClip,
    CompositeVideoClip,
)
import os


# --------------------------------------------------
# Load Overlay Image
# --------------------------------------------------

def load_overlay(image_path, duration, position=("center", "center")):
    """
    Load an overlay image.
    """
    if not os.path.exists(image_path):
        return None

    overlay = (
        ImageClip(image_path)
        .set_duration(duration)
        .set_position(position)
    )

    return overlay


# --------------------------------------------------
# Add Single Overlay
# --------------------------------------------------

def add_overlay(video_clip, overlay_path, position=("center", "center")):
    """
    Add a single overlay image to the video.
    """
    overlay = load_overlay(
        overlay_path,
        video_clip.duration,
        position
    )

    if overlay is None:
        return video_clip

    return CompositeVideoClip([video_clip, overlay])


# --------------------------------------------------
# Celebration Effects
# --------------------------------------------------

def add_confetti(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/confetti.png"
    )


def add_balloons(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/balloons.png"
    )


def add_fireworks(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/fireworks.png"
    )


def add_hearts(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/hearts.png"
    )


def add_sparkles(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/sparkles.png"
    )


def add_cake(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/cake.png",
        position=("right", "bottom")
    )


def add_gift_boxes(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/gifts.png",
        position=("left", "bottom")
    )


def add_party_lights(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/lights.png"
    )


def add_music_notes(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/music_notes.png"
    )


def add_stickers(video_clip):
    return add_overlay(
        video_clip,
        "assets/overlays/stickers.png"
    )


# --------------------------------------------------
# Apply Multiple Effects
# --------------------------------------------------

def apply_effects(video_clip, effects):
    """
    Apply multiple celebration effects.

    effects example:
    [
        "confetti",
        "balloons",
        "hearts"
    ]
    """

    for effect in effects:

        effect = effect.lower()

        if effect == "confetti":
            video_clip = add_confetti(video_clip)

        elif effect == "balloons":
            video_clip = add_balloons(video_clip)

        elif effect == "fireworks":
            video_clip = add_fireworks(video_clip)

        elif effect == "hearts":
            video_clip = add_hearts(video_clip)

        elif effect == "sparkles":
            video_clip = add_sparkles(video_clip)

        elif effect == "cake":
            video_clip = add_cake(video_clip)

        elif effect == "gift boxes":
            video_clip = add_gift_boxes(video_clip)

        elif effect == "party lights":
            video_clip = add_party_lights(video_clip)

        elif effect == "music notes":
            video_clip = add_music_notes(video_clip)

        elif effect == "stickers":
            video_clip = add_stickers(video_clip)

    return video_clip
