import pytest
from utils.mood_check import check_mood_weather_match

@pytest.mark.parametrize("user_mood, weather_description, expected_result", [
    ("happy", "clear sky", True),
    ("sad", "rainy weather", True),
    ("angry", "stormy conditions", True),
    ("calm", "foggy morning", True),
    ("cheerful", "sunny day", True),
    ("fear", "thunderstorm", True),
    ("disgust", "overcast sky", True),
    ("irritability", "hot and humid", True),
    ("romantic", "partly cloudy", True),
    ("energized", "sunny and clear", True),
    ("positive", "partly cloudy with sun", True),
    ("negative", "rainy and overcast", True),
    ("happy", "rainy weather", False),
    ("sad", "sunny day", False),
    ("angry", "clear sky", False),
    ("calm", "windy conditions", False),
    ("cheerful", "foggy morning", False),
    ("fear", "sunny day", False),
    ("disgust", "cloudy sky", False),
    ("irritability", "clear sky", False),
    ("romantic", "rainy weather", False),
    ("energized", "cloudy sky", False),
    ("positive", "rainy weather", False),
    ("negative", "clear sky", False),
])
def test_check_mood_weather_match(user_mood, weather_description, expected_result):
    assert check_mood_weather_match(user_mood, weather_description) == expected_result
