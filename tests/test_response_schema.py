from utils.response_schema import custom_response


def test_custom_response_is_dict():

    response_content = "This is a custom response."
    status_code = 200
    response = custom_response(response_content, status_code)
    assert isinstance(response, dict)

def test_custom_response_contain_detail():

    response_content = "This is a custom response."
    status_code = 200
    response = custom_response(response_content, status_code)
    assert isinstance(response, dict)
    assert "detail" in response
    assert isinstance(response["detail"], dict)
    assert response["detail"]["message"] == response_content
    assert response["detail"]["status"] == status_code