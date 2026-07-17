# theme_manager.py

THEMES = {
    "Birthday": {
        "background": "assets/backgrounds/birthday.jpg",
        "font": "Arial-Bold",
        "title_color": "yellow",
        "subtitle_color": "white",
        "effects": [
            "confetti",
            "balloons",
            "cake"
        ]
    },

    "Wedding Anniversary": {
        "background": "assets/backgrounds/anniversary.jpg",
        "font": "Times-Bold",
        "title_color": "gold",
        "subtitle_color": "white",
        "effects": [
            "hearts",
            "sparkles"
        ]
    },

    "Graduation": {
        "background": "assets/backgrounds/graduation.jpg",
        "font": "Helvetica-Bold",
        "title_color": "blue",
        "subtitle_color": "white",
        "effects": [
            "confetti",
            "fireworks"
        ]
    },

    "Baby Shower": {
        "background": "assets/backgrounds/baby_shower.jpg",
        "font": "Comic-Sans-MS",
        "title_color": "pink",
        "subtitle_color": "white",
        "effects": [
            "balloons",
            "sparkles"
        ]
    },

    "Father's Day": {
        "background": "assets/backgrounds/fathers_day.jpg",
        "font": "Arial-Bold",
        "title_color": "white",
        "subtitle_color": "lightblue",
        "effects": [
            "gift boxes"
        ]
    },

    "Mother's Day": {
        "background": "assets/backgrounds/mothers_day.jpg",
        "font": "Arial-Bold",
        "title_color": "pink",
        "subtitle_color": "white",
        "effects": [
            "hearts",
            "sparkles"
        ]
    },

    "Valentine's Day": {
        "background": "assets/backgrounds/valentine.jpg",
        "font": "Times-Bold",
        "title_color": "red",
        "subtitle_color": "white",
        "effects": [
            "hearts",
            "sparkles"
        ]
    },

    "Christmas": {
        "background": "assets/backgrounds/christmas.jpg",
        "font": "Arial-Bold",
        "title_color": "green",
        "subtitle_color": "white",
        "effects": [
            "sparkles",
            "gift boxes"
        ]
    },

    "New Year": {
        "background": "assets/backgrounds/new_year.jpg",
        "font": "Arial-Bold",
        "title_color": "gold",
        "subtitle_color": "white",
        "effects": [
            "fireworks",
            "confetti"
        ]
    },

    "Retirement": {
        "background": "assets/backgrounds/retirement.jpg",
        "font": "Helvetica-Bold",
        "title_color": "gold",
        "subtitle_color": "white",
        "effects": [
            "sparkles"
        ]
    },

    "Farewell": {
        "background": "assets/backgrounds/farewell.jpg",
        "font": "Arial-Bold",
        "title_color": "white",
        "subtitle_color": "yellow",
        "effects": [
            "confetti"
        ]
    },

    "Festival Greetings": {
        "background": "assets/backgrounds/festival.jpg",
        "font": "Arial-Bold",
        "title_color": "orange",
        "subtitle_color": "white",
        "effects": [
            "fireworks",
            "lights",
            "sparkles"
        ]
    },

    "Wedding Invitation": {
        "background": "assets/backgrounds/wedding.jpg",
        "font": "Times-Bold",
        "title_color": "gold",
        "subtitle_color": "white",
        "effects": [
            "hearts",
            "sparkles"
        ]
    },

    "Achievement": {
        "background": "assets/backgrounds/achievement.jpg",
        "font": "Helvetica-Bold",
        "title_color": "gold",
        "subtitle_color": "white",
        "effects": [
            "confetti",
            "fireworks"
        ]
    },

    "Custom": {
        "background": "",
        "font": "Arial",
        "title_color": "white",
        "subtitle_color": "white",
        "effects": []
    }
}


def get_theme(theme_name):
    """
    Return theme settings.
    """
    return THEMES.get(theme_name, THEMES["Custom"])


def get_theme_list():
    """
    Return available theme names.
    """
    return list(THEMES.keys())


def get_theme_effects(theme_name):
    """
    Return default effects for a theme.
    """
    return get_theme(theme_name)["effects"]


def get_theme_background(theme_name):
    """
    Return background image path.
    """
    return get_theme(theme_name)["background"]


def get_theme_font(theme_name):
    """
    Return font name.
    """
    return get_theme(theme_name)["font"]


def get_title_color(theme_name):
    """
    Return title color.
    """
    return get_theme(theme_name)["title_color"]


def get_subtitle_color(theme_name):
    """
    Return subtitle color.
    """
    return get_theme(theme_name)["subtitle_color"]
