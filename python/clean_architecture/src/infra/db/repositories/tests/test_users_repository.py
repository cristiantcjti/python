import uuid
import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.users_repository import UsersRepository


class TestUsersRespository:
    DB_CONNECTION_HANDLER = DBConnectionHandler()
    CONNECTION = DB_CONNECTION_HANDLER.get_engine().connect()

    @pytest.mark.skip(reason="Sensive test")
    def test_insert_user(self):
        mocked_first_name = "first"
        mocked_last_name = "last"
        mocked_age = 51

        users_repository = UsersRepository()
        users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

        sql = f"""
            SELECT * FROM public.users
            WHERE first_name = '{mocked_first_name}'
            AND last_name = '{mocked_last_name}'
            AND age = {mocked_age}
        """
        response = self.CONNECTION.execute(text(sql))
        registry = response.fetchall()[8]

        assert registry.first_name == mocked_first_name
        assert registry.last_name == mocked_last_name
        assert registry.age == mocked_age

        self.CONNECTION.execute(
            text(f"""
            DELETE FROM public.users WHERE id = '{registry.id}'
        """)
        )
        self.CONNECTION.commit()

    @pytest.mark.skip(reason="Sensive test")
    def test_select_user(self):
        mocked_first_name = "first_2"
        mocked_last_name = "last_2"
        mocked_age = 51

        sql = f"""
            INSERT INTO users (id, first_name, last_name, age) VALUES (
                '{uuid.uuid4()}',
                '{mocked_first_name}',
                '{mocked_last_name}',
                {mocked_age}
            )
        """
        self.CONNECTION.execute(text(sql))
        self.CONNECTION.commit()

        users_repository = UsersRepository()
        response = users_repository.select_user(mocked_first_name)

        assert response[0].first_name == mocked_first_name
        assert response[0].last_name == mocked_last_name
        assert response[0].age == mocked_age

        self.CONNECTION.execute(
            text(f"""
            DELETE FROM users WHERE id = '{response[0].id}'
        """)
        )
        self.CONNECTION.commit()
