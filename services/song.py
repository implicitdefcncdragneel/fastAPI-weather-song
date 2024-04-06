import os

import httpx
from fastapi import HTTPException, status

from exception.last_fm_exception import (
    raise_last_fm_api_key_error,
    raise_last_fm_bad_request_error,
    raise_last_fm_generic_error,
)
from open_api_url.audio_scrobbler import AudioScrobblerUrls

API_KEY = os.environ.get("AUDIO_API_KEY")

async def get_song(mood: str):
    """Retrieve a list of songs based on the user's mood.

    Args:
        mood (str): Current mood of the user

    Returns:
        List[str]: An array containing names of songs from different albums.
    """
    async with httpx.AsyncClient(base_url=AudioScrobblerUrls.BASE_URL) as client: 
        
        params_dict = {
            "method": "album.search",
            "api_key": API_KEY,
            "album": mood,
            "format" : "json"
        }
        try:
            response = await client.get(AudioScrobblerUrls.v2, params=params_dict)
            response.raise_for_status() #raise an exception for any responses which are not a 2xx success code.
            album_json_response = response.json()
            album_list  = album_json_response["results"]["albummatches"]["album"]
            names = [album["name"] for album in album_list if album.get("name")]
            return names
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                raise raise_last_fm_bad_request_error()
            elif e.response.status_code == 403:
                raise raise_last_fm_api_key_error()
            else:
                raise raise_last_fm_generic_error()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="LastFM Service: Internal Server Error")