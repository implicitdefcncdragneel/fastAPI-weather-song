import pytest
from fastapi import HTTPException

from services.weather import get_current_weather, get_geo_location

city_name = "Bengaluru"
mock_base_url = "http://127.0.0.1:3000"
lat = 11.1111
lon = 22.2222

@pytest.mark.asyncio
async def test_get_weather_pass():
    mock_endpoint = "/mockWeatherGeo"
    location = await get_geo_location(city_name, mock_base_url, mock_endpoint)
    assert location[0] == lat
    assert location[1] == lon

@pytest.mark.asyncio
async def test_get_weather_400_error():
    mock_endpoint = "/mock400"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_weather_401_error():
    mock_endpoint = "/mock401"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_weather_404_error():
    mock_endpoint = "/mock404"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_weather_429_error():
    mock_endpoint = "/mock429"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_weather_500_error():
    mock_endpoint = "/mock500"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_weather_internal_server_error():
    mock_base_url = mock_base_url = "http://127.0.0.1:3333"
    with pytest.raises(HTTPException):
        await get_geo_location(city_name, mock_base_url)

@pytest.mark.asyncio
async def test_get_current_weather_pass():
    mock_endpoint = "/mockWeatherDescription"
    current_weather = await get_current_weather(lat, lon, mock_base_url, mock_endpoint)
    assert current_weather == 'Clear sky'

@pytest.mark.asyncio
async def test_get_current_weather_400_error():
    mock_endpoint = "/mock400"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_current_weather_401_error():
    mock_endpoint = "/mock401"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_current_weather_404_error():
    mock_endpoint = "/mock404"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_current_weather_429_error():
    mock_endpoint = "/mock429"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_current_weather_500_error():
    mock_endpoint = "/mock500"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_current_weather_internal_server_error():
    mock_base_url = mock_base_url = "http://127.0.0.1:3333"
    with pytest.raises(HTTPException):
        await get_current_weather(lat, lon, mock_base_url)