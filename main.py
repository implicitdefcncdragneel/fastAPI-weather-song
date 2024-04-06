from dotenv import load_dotenv
from fastapi import FastAPI
from routers.song_recommendation import router as song_router

load_dotenv()

app = FastAPI()
app.include_router(song_router)