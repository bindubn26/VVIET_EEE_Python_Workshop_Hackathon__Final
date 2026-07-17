import os


RESOLUTIONS = {
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "2K": (2560, 1440),
    "4K": (3840, 2160),
}


FORMATS = {
    "MP4": {
        "extension": ".mp4",
        "codec": "libx264",
        "audio_codec": "aac"
    },
    "MOV": {
        "extension": ".mov",
        "codec": "libx264",
        "audio_codec": "aac"
    },
    "AVI": {
        "extension": ".avi",
        "codec": "png",
        "audio_codec": "pcm_s16le"
    },
    "WEBM": {
        "extension": ".webm",
        "codec": "libvpx",
        "audio_codec": "libvorbis"
    }
}


def get_resolution(name):
    """
    Return (width, height)
    """
    return RESOLUTIONS.get(name, (1280, 720))


def resize_video(video, resolution="720p"):
    """
    Resize video to selected resolution.
    """
    size = get_resolution(resolution)
    return video.resize(size)


def export_video(
    video,
    output_name="Celebration_Video",
    export_format="MP4",
    resolution="1080p",
    fps=30,
    output_folder="outputs"
):
    """
    Export final celebration video.
    """

    os.makedirs(output_folder, exist_ok=True)

    video = resize_video(video, resolution)

    settings = FORMATS.get(export_format.upper(), FORMATS["MP4"])

    filename = output_name + settings["extension"]

    output_path = os.path.join(
        output_folder,
        filename
    )

    video.write_videofile(
        output_path,
        codec=settings["codec"],
        audio_codec=settings["audio_codec"],
        fps=fps
    )

    return output_path


def available_formats():
    return list(FORMATS.keys())


def available_resolutions():
    return list(RESOLUTIONS.keys())
