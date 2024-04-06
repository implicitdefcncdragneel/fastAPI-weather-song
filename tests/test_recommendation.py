from unittest.mock import MagicMock, patch

import pytest

from routers.recommendation import song_recommendation

city_name = "Bengaluru"
current_mood = "happy"
latitude, longitude = 11.1111, 22.2222

@pytest.mark.asyncio
@patch('services.weather.get_geo_location', MagicMock(return_value=(latitude, longitude)))
@patch('services.weather.get_current_weather', MagicMock(return_value="Clear sky"))
@patch('services.song.get_song', MagicMock(return_value=["Happy Song 1", "Happy Song 2"]))
async def test_song_recommendation_pass():
    response = await song_recommendation(city_name, current_mood)
    assert response