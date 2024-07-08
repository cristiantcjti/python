from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UsersRepositoryInterface):
        self._user_repository = user_repository

    @classmethod
    def _validate_name(cls, first_name: str):
        if not first_name.isalpha():
            raise Exception("Invalid name for searching")

        if len(first_name) > 18:
            raise Exception("Name too long")

    def _registry_user_information(
        self, first_name: str, last_name: str, age: int
    ) -> None:
        self._user_repository.insert_user(first_name, last_name, age)

    @classmethod
    def _format_response(cls, first_name: str, last_name: str, age: int) -> dict:
        return {
            "type": "users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            },
        }

    def register(self, first_name: str, last_name: str, age: int) -> dict:
        self._validate_name(first_name)
        self._validate_name(last_name)
        self._registry_user_information(first_name, last_name, age)
        return self._format_response(first_name, last_name, age)
