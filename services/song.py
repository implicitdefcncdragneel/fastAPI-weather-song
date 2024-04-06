import httpx,os
from fastapi import HTTPException
from utils.urls import AudioScrobblerUrls

API_KEY = os.environ.get("AUDIO_API_KEY")

async def get_song(mood: str):
    async with httpx.AsyncClient(base_url=AudioScrobblerUrls.BASE_URL) as client:
        
        params_dict = {
            "method": "album.search",
            "api_key": API_KEY,
            "album": mood,
            "format" : "json"
        }
        try:
            response = await client.get(AudioScrobblerUrls.v2, params=params_dict)
            response.raise_for_status()
            album_json_response = response.json()
            album_list  = album_json_response["results"]["albummatches"]["album"]
            names = [album["name"] for album in album_list if album.get("name")]
            return names
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json()["message"])
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))