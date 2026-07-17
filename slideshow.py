from moviepy.editor import (
    ImageClip,
    concatenate_videoclips,
    vfx
)
import os


# --------------------------------------------
# Resize Images
# --------------------------------------------

def resize_clip(clip, size=(1280, 720)):
    return clip.resize(size)


# --------------------------------------------
# Zoom Effect
# --------------------------------------------

def zoom_effect(clip):
    return clip.fx(vfx.resize, lambda t: 1 + 0.04 * t)


# --------------------------------------------
# Fade Effect
# --------------------------------------------

def fade_effect(clip):
    return clip.fadein(1).fadeout(1)


# --------------------------------------------
# Rotate Effect
# --------------------------------------------

def rotate_effect(clip):
    return clip.rotate(lambda t: 2 * t)


# --------------------------------------------
# Ken Burns Effect
# --------------------------------------------

def ken_burns_effect(clip):
    return clip.fx(vfx.resize, lambda t: 1 + 0.03 * t)


# --------------------------------------------
# Pan Effect
# --------------------------------------------

def pan_effect(clip):
    return clip.set_position(
        lambda t: (-30 * t, 0)
    )


# --------------------------------------------
# Apply Selected Animation
# --------------------------------------------

def apply_animation(clip, animation):

    animation = animation.lower()

    if animation == "zoom":
        return zoom_effect(clip)

    elif animation == "fade":
        return fade_effect(clip)

    elif animation == "rotate":
        return rotate_effect(clip)

    elif animation == "ken burns":
        return ken_burns_effect(clip)

    elif animation == "pan":
        return pan_effect(clip)

    else:
        return clip


# --------------------------------------------
# Create Slideshow
# --------------------------------------------

def create_slideshow(
    image_paths,
    duration=3,
    animation="Fade",
    size=(1280, 720)
):

    clips = []

    for image in image_paths:

        clip = (
            ImageClip(image)
            .set_duration(duration)
        )

        clip = resize_clip(clip, size)

        clip = apply_animation(
            clip,
            animation
        )

        clips.append(clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    return final_video


# --------------------------------------------
# Export Slideshow
# --------------------------------------------

def export_slideshow(
    image_paths,
    output_path="outputs/slideshow.mp4",
    duration=3,
    animation="Fade",
    fps=30
):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    slideshow = create_slideshow(
        image_paths,
        duration,
        animation
    )

    slideshow.write_videofile(
        output_path,
        fps=fps,
        codec="libx264",
        audio=False
    )

    return output_path
