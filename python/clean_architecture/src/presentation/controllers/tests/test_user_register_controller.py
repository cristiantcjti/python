from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.use_cases.tests.user_register_spy import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self):
        self.body = {"first_name": "MyFirstName", "last_name": "MyLastName", "age": 20}


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)

    response = user_register_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["type"] == "users"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["attributes"][0]["first_name"] == "MyFirstName"
    assert response.body["data"]["attributes"][0]["last_name"] == "MyLastName"
    assert response.body["data"]["attributes"][0]["age"] == 20
