from src.infra.db.repositories.users_repository import UsersRepository


class TestUsersRespository:

    def test_insert_user(self):
        first_name = "first_name"
        last_name = "last_name"
        age = 35

        users_repository = UsersRepository()
        users_repository.insert_user(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
