from typing import Dict, Optional
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self._users_repository = users_repository

    @classmethod
    def _validate_name(cls, first_name: str):
        if not first_name.isalpha():
            raise Exception("Invalid name for searching")

        if len(first_name) > 18:
            raise Exception("Name too long")

    def _search_user(self, first_name: str) -> list[Users]:
        users = self._users_repository.select_user(first_name)
        if users == []:
            raise Exception("User not found")
        return users

    @classmethod
    def _format_response(cls, users: list[Users]) -> dict:
        users = [{"first_name": user.first_name, "age": user.age} for user in users]
        return {"type": "users", "count": len(users), "attributes": users}

    def find(self, first_name: str) -> Dict:
        self._validate_name(first_name)
        users = self._search_user(first_name)
        return self._format_response(users)
