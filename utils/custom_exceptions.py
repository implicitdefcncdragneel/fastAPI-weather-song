import time
from fastapi import HTTPException,status

def raise_rate_limiter_exceeded_exception(second_of_generated_request,second_to_wait):
    """Raise an exception when the API call limit is exceeded.

    Args:
        second_of_generated_request (float): The timestamp when the request was generated.
        second_to_wait (int): Defined waiting time for each API call.

    Returns:
        HTTPException: Exception raised.
    """

    second_to_wait = round((second_of_generated_request+second_to_wait) - time.time())

    detail = {
        "message":f"Please wait and retry after {second_to_wait} second",
        "status":status.HTTP_429_TOO_MANY_REQUESTS
    }

    return HTTPException(status_code=detail["status"], detail=detail)

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


def raise_last_fm_bad_request_error():
    """
    Raises an HTTPException with status code 400 for Last FM API indicating a bad request.

    Returns:
        HTTPException: An instance of HTTPException with status code 400 and detail message.
    """
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Last FM: Invalid parameter or method")

def raise_last_fm_api_key_error():
    """
    Raises an HTTPException with status code 403 for Last FM API indicating an invalid API key.

    Returns:
        HTTPException: An instance of HTTPException with status code 403 and detail message.
    """
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Last FM: Invalid API Key")

def raise_last_fm_generic_error():
    """
    Raises an HTTPException with status code 500 for Last FM API indicating an internal server error.

    Returns:
        HTTPException: An instance of HTTPException with status code 500 and detail message.
    """
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Last FM: Internal Server Error")