# from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder


class TestUserFinder:
    def test_find(self):
        repo = UsersRepository()
        user_finder = UserFinder(repo)
        print(user_finder)
        assert 1 == 4
