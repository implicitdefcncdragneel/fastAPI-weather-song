
def check_mood_weather_match(user_mood: str, weather_description: str) -> bool:

    mood_weather_mapping = {
        "happy": ["clear", "sun", "clouds"],
        "sad": ["rain", "drizzle", "thunderstorm"],
        "angry": ["storm", "thunderstorm", "wind"],
        "calm": ["clear", "clouds", "mist", "fog"],
        "cheerful": ["clear", "sun"],
        "fear": ["fog", "mist", "rain", "thunderstorm"],
        "disgust": ["fog", "mist", "rain", "overcast"],
        "irritability": ["hot", "humid", "overcast"],
        "romantic": ["partly cloudy", "clear"],
        "energized": ["partly cloudy", "clear", "sun"],
        "positive": ["clear", "sun", "partly cloudy"],
        "angry": ["storm", "thunderstorm", "wind"],
        "negative": ["fog", "rain", "overcast"]
    }

    for mood, weather_conditions in mood_weather_mapping.items():
        if user_mood.lower() == mood:
            if any(condition in weather_description.lower() for condition in weather_conditions):
                return True
    return False