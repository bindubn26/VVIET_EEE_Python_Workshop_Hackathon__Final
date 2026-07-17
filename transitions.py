from moviepy.editor import concatenate_videoclips


# -----------------------------------------
# No Transition
# -----------------------------------------

def no_transition(clips):
    """
    Join clips without transitions.
    """
    return concatenate_videoclips(
        clips,
        method="compose"
    )


# -----------------------------------------
# Fade Transition
# -----------------------------------------

def fade_transition(clips, duration=1):
    """
    Fade transition between clips.
    """
    transition_clips = []

    for clip in clips:
        transition_clips.append(
            clip.crossfadein(duration)
        )

    return concatenate_videoclips(
        transition_clips,
        method="compose",
        padding=-duration
    )


# -----------------------------------------
# Cross Fade
# -----------------------------------------

def cross_fade(clips, duration=1):

    transition_clips = []

    for clip in clips:
        transition_clips.append(
            clip.crossfadein(duration)
        )

    return concatenate_videoclips(
        transition_clips,
        method="compose",
        padding=-duration
    )


# -----------------------------------------
# Slide Left
# -----------------------------------------

def slide_left(clips):

    animated = []

    for clip in clips:

        c = clip.set_position(
            lambda t: (-150 * t, 0)
        )

        animated.append(c)

    return concatenate_videoclips(
        animated,
        method="compose"
    )


# -----------------------------------------
# Slide Right
# -----------------------------------------

def slide_right(clips):

    animated = []

    for clip in clips:

        c = clip.set_position(
            lambda t: (150 * t, 0)
        )

        animated.append(c)

    return concatenate_videoclips(
        animated,
        method="compose"
    )


# -----------------------------------------
# Zoom Transition
# -----------------------------------------

def zoom_transition(clips):

    animated = []

    for clip in clips:

        c = clip.resize(
            lambda t: 1 + 0.04 * t
        )

        animated.append(c)

    return concatenate_videoclips(
        animated,
        method="compose"
    )


# -----------------------------------------
# Blur Transition
# -----------------------------------------

def blur_transition(clips):
    """
    Placeholder for blur transition.
    Currently behaves like normal transition.
    """

    return concatenate_videoclips(
        clips,
        method="compose"
    )


# -----------------------------------------
# Rotate Transition
# -----------------------------------------

def rotate_transition(clips):

    animated = []

    for clip in clips:

        c = clip.rotate(
            lambda t: 2 * t
        )

        animated.append(c)

    return concatenate_videoclips(
        animated,
        method="compose"
    )


# -----------------------------------------
# Apply Transition
# -----------------------------------------

def apply_transition(
    clips,
    transition="Fade"
):

    transition = transition.lower()

    if transition == "fade":
        return fade_transition(clips)

    elif transition == "cross fade":
        return cross_fade(clips)

    elif transition == "slide left":
        return slide_left(clips)

    elif transition == "slide right":
        return slide_right(clips)

    elif transition == "zoom":
        return zoom_transition(clips)

    elif transition == "blur":
        return blur_transition(clips)

    elif transition == "rotate":
        return rotate_transition(clips)

    else:
        return no_transition(clips)
