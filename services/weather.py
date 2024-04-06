import httpx,os
from fastapi import HTTPException,status #https://fastapi.tiangolo.com/reference/apirouter/
from utils.custom_exceptions import raise_open_weather_api_key_error, raise_open_weather_bad_request_error, raise_open_weather_generic_error, raise_open_weather_limit_exceeded_error, raise_open_weather_not_found_error
from utils.urls import OpenWeatherMapUrls

WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")

async def get_geo_location(city_name: str):
    """Retrieve the latitude and longitude of a given city.

    Args:
        city_name (str): The name of the city.

    Returns:
        Tuple[float, float]: A tuple containing the latitude and longitude of the city.
    """
    async with httpx.AsyncClient(base_url=OpenWeatherMapUrls.BASE_URL) as client:
        params_dict = {
            "q": city_name,
            "appid": WEATHER_API_KEY
        }
        try:
            response = await client.get(OpenWeatherMapUrls.GEO_API["LOCATION_URL"], params=params_dict)
            response.raise_for_status() #raise an exception for any responses which are not a 2xx success code.
            location_json_response = response.json()
            latitude, longitude = location_json_response[0]["lat"], location_json_response[0]["lon"]
            return latitude, longitude
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                raise raise_open_weather_bad_request_error()
            elif e.response.status_code == 401:
                raise raise_open_weather_api_key_error()
            elif e.response.status_code == 404:
                raise raise_open_weather_not_found_error()
            elif e.response.status_code == 429:
                raise raise_open_weather_limit_exceeded_error()
            else:
                raise raise_open_weather_generic_error()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Weather Service Internal Server Error")

async def get_current_weather(latitude: str, longitude: str):
    """Retrieve the current weather description based on latitude and longitude.

    Args:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location

    Returns:
        str: The current weather description.
    """
    async with httpx.AsyncClient(base_url=OpenWeatherMapUrls.BASE_URL) as client:
        params_dict = {
            "lat": latitude,
            "lon": longitude,
            "appid": WEATHER_API_KEY
        }
        try:
            response = await client.get(OpenWeatherMapUrls.DATA_API["WEATHER_URL"], params=params_dict)
            response.raise_for_status() #raise an exception for any responses which are not a 2xx success code.
            weather_json_response = response.json()
            weather_description = weather_json_response["weather"][0]["description"]
            return weather_description
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                raise raise_open_weather_bad_request_error()
            elif e.response.status_code == 401:
                raise raise_open_weather_api_key_error()
            elif e.response.status_code == 404:
                raise raise_open_weather_not_found_error()
            elif e.response.status_code == 429:
                raise raise_open_weather_limit_exceeded_error()
            else:
                raise raise_open_weather_generic_error()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Weather Service Internal Server Error")