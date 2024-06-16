import pytest
from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_finder import UserFinder


class TestUserFinder:
    def test_find(self):
        first_name = "NameTest"

        repo = UsersRepositorySpy()
        user_finder = UserFinder(repo)

        response = user_finder.find(first_name)

        assert repo.select_user_attributes["first_name"] == first_name
        assert response["type"] == "users"
        assert response["count"] == len(response["attributes"])
        assert response["attributes"] != []

    def test_find_error_in_valid_name(self):
        first_name = "NameTest123"
        repo = UsersRepositorySpy()
        user_finder = UserFinder(repo)

        with pytest.raises(Exception) as error:
            user_finder.find(first_name)

        assert str(error.value) == "Invalid name for searching"

    def test_find_error_in_name_too_long(self):
        first_name = "TestNameTooLongInMethodFind"
        repo = UsersRepositorySpy()
        user_finder = UserFinder(repo)

        with pytest.raises(Exception) as error:
            user_finder.find(first_name)

        assert str(error.value) == "Name too long"

    def test_find_error_user_not_found(self, mocker):
        first_name = "TestName"
        UsersRepositorySpy.select_user = mocker.Mock(return_value=[])
        repo = UsersRepositorySpy()
        user_finder = UserFinder(repo)

        with pytest.raises(Exception) as error:
            user_finder.find(first_name)

        assert str(error.value) == "User not found"
