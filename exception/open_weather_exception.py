from fastapi import HTTPException, status

# https://openweathermap.org/api/one-call-3#errors
def raise_open_weather_bad_request_error():
    """
    Raises an HTTPException with status code 400 for OpenWeather API indicating a bad request.

    Returns:
        HTTPException: An instance of HTTPException with status code 400 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="OpenWeather: Bad value entered")

def raise_open_weather_api_key_error():
    """
    Raises an HTTPException with status code 401 for OpenWeather API indicating an invalid API key.

    Returns:
        HTTPException: An instance of HTTPException with status code 401 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="OpenWeather: Invalid API Key")

def raise_open_weather_not_found_error():
    """
    Raises an HTTPException with status code 404 for OpenWeather API indicating not found.

    Returns:
        HTTPException: An instance of HTTPException with status code 404 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OpenWeather: lat,lon,date does not exist")

def raise_open_weather_limit_exceeded_error():
    """
    Raises an HTTPException with status code 429 for OpenWeather API indicating API limit exceeded.

    Returns:
        HTTPException: An instance of HTTPException with status code 429 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="OpenWeather: API Limit Exceeded")

def raise_open_weather_generic_error():
    """
    Raises an HTTPException with status code 500 for OpenWeather API indicating an internal server error.

    Returns:
        HTTPException: An instance of HTTPException with status code 500 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="OpenWeather: Internal Server Error")