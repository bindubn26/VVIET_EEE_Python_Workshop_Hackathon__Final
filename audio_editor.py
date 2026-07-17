from pydub import AudioSegment
import os


def load_audio(file_path):
    """
    Load MP3 or WAV audio.
    """
    if file_path.lower().endswith(".mp3"):
        return AudioSegment.from_mp3(file_path)
    elif file_path.lower().endswith(".wav"):
        return AudioSegment.from_wav(file_path)
    else:
        raise ValueError("Unsupported audio format")


def merge_audio(audio_list):
    """
    Merge multiple audio files.
    """
    if not audio_list:
        return None

    merged = audio_list[0]

    for audio in audio_list[1:]:
        merged += audio

    return merged


def trim_audio(audio, start_sec, end_sec):
    """
    Trim audio.
    """
    start = start_sec * 1000
    end = end_sec * 1000

    return audio[start:end]


def fade_in(audio, seconds):
    """
    Apply fade in.
    """
    return audio.fade_in(seconds * 1000)


def fade_out(audio, seconds):
    """
    Apply fade out.
    """
    return audio.fade_out(seconds * 1000)


def change_volume(audio, volume_db):
    """
    Increase or decrease volume.
    Positive = louder
    Negative = quieter
    """
    return audio + volume_db


def loop_audio(audio, total_duration_ms):
    """
    Loop audio until required duration.
    """
    output = audio

    while len(output) < total_duration_ms:
        output += audio

    return output[:total_duration_ms]


def mix_voice_and_music(voice, music, music_volume=-15):
    """
    Overlay voice on background music.
    """
    music = music + music_volume
    return music.overlay(voice)


def export_audio(audio, output_path):
    """
    Export final audio.
    """
    audio.export(output_path, format="mp3")
    return output_path


def prepare_audio(
    voice_path=None,
    music_path=None,
    output_path="outputs/final_audio.mp3"
):
    """
    Complete audio pipeline.
    """

    if voice_path and music_path:

        voice = load_audio(voice_path)
        music = load_audio(music_path)

        music = loop_audio(music, len(voice))
        music = fade_in(music, 2)
        music = fade_out(music, 2)

        final_audio = mix_voice_and_music(
            voice,
            music
        )

    elif voice_path:

        final_audio = load_audio(voice_path)

    elif music_path:

        final_audio = load_audio(music_path)

    else:
        return None

    export_audio(final_audio, output_path)

    return output_path
