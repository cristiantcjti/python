import pytest
from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_register import UserRegister


class TestUserRegister:
    def test_register(self):
        first_name = "NameTest"
        last_name = "LastNameTest"
        age = 25

        repository = UsersRepositorySpy()
        user_register = UserRegister(repository)
        response = user_register.register(first_name, last_name, age)

        assert response["type"] == "users"
        assert response["count"] == 1
        assert response["attributes"]["first_name"] == first_name
        assert response["attributes"]["last_name"] == last_name
        assert response["attributes"]["age"] == age

    def test_find_error_in_valid_name(self):
        first_name = "NameTest123"
        last_name = "LastNameTest"
        age = 25
        expected_error_message = "Invalid name for searching"

        repo = UsersRepositorySpy()
        user_register = UserRegister(repo)

        with pytest.raises(Exception) as error:
            user_register.register(first_name, last_name, age)

        assert str(error.value) == expected_error_message
