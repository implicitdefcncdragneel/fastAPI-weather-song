from fastapi import HTTPException, status


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