import httpx
import os
from utils.urls import OpenWeatherMapUrls

API_KEY = os.getenv("API_KEY", "API_KEY")

def get_geo_location(city_name : str):
    '''
    fetch latitude, longitude based on city_name
    '''

    #https://www.python-httpx.org/advanced/clients/
    with httpx.Client(base_url = OpenWeatherMapUrls.BASE_URL) as client:
        
        params_dict = {
                        "q": city_name, 
                        "appid": API_KEY
                    }

        try:
            response = client.get(OpenWeatherMapUrls.GEO_API["LOCATION_URL"],params = params_dict)
            location_json_response = response.json()

            latitude,longitude = location_json_response[0]["lat"],location_json_response[0]["lon"]
            
            return [latitude, longitude]
        except Exception as err:
            #TODO: Handle it
            print(f'Other error occurred: {err}')

def get_weather_forecast(latitude : str,longitude : str):
    '''
    fetch weather forecaset
    '''
    with httpx.Client(base_url = OpenWeatherMapUrls.BASE_URL) as client:
        
        params_dict = {
                        "lat": latitude, 
                        "lon": longitude,
                        "appid": API_KEY
                    }

        try:
            response = client.get(OpenWeatherMapUrls.DATA_API["FORECAST_URL"],params = params_dict)
            forecase_json_response = response.json()
            #TODO:
            return
        except Exception as err:
            #TODO: Handle it
            print(f'Other error occurred: {err}')