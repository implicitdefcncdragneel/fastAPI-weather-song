from fastapi import (  # https://fastapi.tiangolo.com/reference/apirouter/
    APIRouter,
    status,
)

from services.song import get_song
from services.weather import get_current_weather, get_geo_location
from utils.mood_check import check_mood_weather_match
from utils.rate_limitter import rate_limited
from utils.response_schema import custom_response

router = APIRouter(
    prefix="/song",
)

@router.get("/")
@rate_limited(max_calls=2,time_frame=120)
async def song_recommendation(city_name: str,current_mood: str):
    """Get weather related information and suggest songs based on the user's mood and the current weather.

    Args:
        city_name (str): The name of the city for which weather information is requested.
        current_mood (str): The current mood of the user.

    Returns:
        List[str]: An array containing names of songs suggested based on the user's mood or the current weather.
    """
    latitude, longitude = await get_geo_location(city_name)
    weather_description = await get_current_weather(latitude, longitude)
    result = weather_description if check_mood_weather_match(current_mood, weather_description) else current_mood #return song based on weather condition or user mood(can be invalid mood)
    respone = await get_song(result)
    return custom_response(respone,status.HTTP_200_OK) if respone else custom_response("Cannot recommend song this time",status.HTTP_200_OK)