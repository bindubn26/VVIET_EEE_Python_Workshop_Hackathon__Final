from gtts import gTTS
import os


LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Telugu": "te",
    "Tamil": "ta",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn"
}


def generate_ai_voice(
    text,
    language="English",
    output_path="outputs/ai_voice.mp3"
):
    """
    Generate AI voice using gTTS.
    """

    if text.strip() == "":
        return None

    lang = LANGUAGE_CODES.get(language, "en")

    tts = gTTS(
        text=text,
        lang=lang,
        slow=False
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    tts.save(output_path)

    return output_path


def birthday_message(name):
    return (
        f"Happy Birthday {name}! "
        "Wishing you happiness, success, good health "
        "and countless wonderful memories."
    )


def anniversary_message(name):
    return (
        f"Happy Wedding Anniversary {name}! "
        "May your life together always be filled with love, "
        "joy and beautiful memories."
    )


def graduation_message(name):
    return (
        f"Congratulations {name}! "
        "Your hard work has paid off. "
        "Wishing you success in every step of your future."
    )


def retirement_message(name):
    return (
        f"Congratulations on your retirement {name}! "
        "May this new journey bring peace, happiness "
        "and wonderful experiences."
    )


def custom_message(event, name):
    return (
        f"Congratulations {name}! "
        f"Best wishes for your {event}. "
        "May this special occasion bring happiness "
        "and unforgettable memories."
    )


def generate_event_voice(
    event,
    name,
    language="English"
):
    """
    Generate AI voice based on event type.
    """

    event = event.lower()

    if event == "birthday":
        text = birthday_message(name)

    elif event == "wedding anniversary":
        text = anniversary_message(name)

    elif event == "graduation":
        text = graduation_message(name)

    elif event == "retirement":
        text = retirement_message(name)

    else:
        text = custom_message(event, name)

    return generate_ai_voice(
        text=text,
        language=language,
        output_path="outputs/event_voice.mp3"
    )


def save_custom_voice(
    message,
    language="English"
):
    """
    Generate voice from user-entered message.
    """

    return generate_ai_voice(
        text=message,
        language=language,
        output_path="outputs/custom_voice.mp3"
    )
