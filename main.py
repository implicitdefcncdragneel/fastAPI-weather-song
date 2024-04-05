from fastapi import FastAPI
from routers.recommendation import router as recommendation_router

app = FastAPI()
app.include_router(recommendation_router)