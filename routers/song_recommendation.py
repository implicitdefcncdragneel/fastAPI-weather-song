from fastapi import APIRouter, HTTPException #https://fastapi.tiangolo.com/reference/apirouter/
from services.song import get_song
from services.weather import get_current_weather, get_geo_location
from utils.mood_check import check_mood_weather_match

router = APIRouter(
    prefix="/song",
)

@router.get("/")
async def get_weather(city_name: str,current_mood: str):
    try:
        latitude, longitude = await get_geo_location(city_name)
        weather_description = await get_current_weather(latitude, longitude)
        if check_mood_weather_match(current_mood,weather_description):
            result = await get_song(weather_description)
        else:
            result = await get_song(current_mood)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))