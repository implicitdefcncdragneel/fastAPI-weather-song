from fastapi import APIRouter #https://fastapi.tiangolo.com/reference/apirouter/

router = APIRouter(
    prefix="/recommendation",
)

@router.get("/")
def read_root():
    return {
            "message": "recommendation is running"
            }