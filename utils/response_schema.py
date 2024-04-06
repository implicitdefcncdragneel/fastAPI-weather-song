def custom_response(response_content,status_code):

    response = {"detail":{
                    "message":response_content,
                    "status":status_code
                }}
    return response