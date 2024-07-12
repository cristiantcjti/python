from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.use_cases.tests.user_finder_spy import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self):
        self.query_params = {"first_name": "myTest"}


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["type"] == "users"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["attributes"][0]["first_name"] == "John"
    assert response.body["data"]["attributes"][0]["age"] == 25
