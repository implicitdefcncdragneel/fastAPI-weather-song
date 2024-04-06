class OpenWeatherMapUrls:

    """
    Class containing URLs for accessing OpenWeatherMap APIs.
    """

    BASE_URL  = "https://api.openweathermap.org"

    GEO_API = {
        "LOCATION_URL": "/geo/1.0/direct",
    }

    DATA_API = {
        "WEATHER_URL": "/data/2.5/weather",
    }