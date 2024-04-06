import time

from fastapi import HTTPException, status


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