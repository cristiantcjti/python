from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self._users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        if not first_name.isalpha():
            raise Exception("Invalid name for searching")

        if len(first_name) > 18:
            raise Exception("Name too long")

        users = self._users_repository.select_user(first_name)
        if users == []:
            raise Exception("User not found")

        return {"type": "users", "count": len(users), "attributes": users}
