import httpx,os
from fastapi import HTTPException #https://fastapi.tiangolo.com/reference/apirouter/
from utils.urls import OpenWeatherMapUrls

WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")

async def get_geo_location(city_name: str):
    async with httpx.AsyncClient(base_url=OpenWeatherMapUrls.BASE_URL) as client:
        params_dict = {
            "q": city_name,
            "appid": WEATHER_API_KEY
        }
        try:
            response = await client.get(OpenWeatherMapUrls.GEO_API["LOCATION_URL"], params=params_dict)
            response.raise_for_status()
            location_json_response = response.json()
            latitude, longitude = location_json_response[0]["lat"], location_json_response[0]["lon"]
            return latitude, longitude
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json()["message"])
        except Exception as e:
            raise HTTPException(status_code=501, detail=str(e))

async def get_current_weather(latitude: str, longitude: str):
    async with httpx.AsyncClient(base_url=OpenWeatherMapUrls.BASE_URL) as client:
        params_dict = {
            "lat": latitude,
            "lon": longitude,
            "appid": WEATHER_API_KEY
        }
        try:
            response = await client.get(OpenWeatherMapUrls.DATA_API["WEATHER_URL"], params=params_dict)
            response.raise_for_status()
            weather_json_response = response.json()
            weather_description = weather_json_response["weather"][0]["description"]
            return weather_description
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json()["message"])
        except Exception as e:
            raise HTTPException(status_code=502, detail=str(e))