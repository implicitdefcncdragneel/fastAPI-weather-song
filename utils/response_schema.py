
def custom_response(response_content,status_code):

    """Generates a custom response with the provided response content and status code.

    Args:
        response_content (str): Message/content of the response.
        status_code (int): HTTP status code of the response.

    Returns:
        dict: custom response
    """
    response = {
        "detail":{
                    "message": response_content,
                    "status": status_code
                }}
    return response