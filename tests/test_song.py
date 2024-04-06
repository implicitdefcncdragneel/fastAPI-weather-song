import pytest
from fastapi import HTTPException

from services.song import get_song

mood = "happy"
mock_base_url = "http://127.0.0.1:3000"

@pytest.mark.asyncio
async def test_get_song_pass():
    mock_endpoint = "/mockSongSuccess"
    songs = await get_song(mood, mock_base_url, mock_endpoint)
    assert songs == ["Happy Album 1", "Happy Album 2"]

@pytest.mark.asyncio
async def test_get_song_400_error():
    mock_endpoint = "/mock400"
    with pytest.raises(HTTPException):
        await get_song(mood, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_song_403_error():
    mock_endpoint = "/mock403"
    with pytest.raises(HTTPException):
        await get_song(mood, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_song_500_error():
    mock_endpoint = "/mock500"
    with pytest.raises(HTTPException):
        await get_song(mood, mock_base_url, mock_endpoint)

@pytest.mark.asyncio
async def test_get_song_internal_server_error():
    mock_base_url = mock_base_url = "http://127.0.0.1:3333"
    with pytest.raises(HTTPException):
        await get_song(mood, mock_base_url)