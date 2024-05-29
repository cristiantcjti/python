import pytest
from ..connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensitive test")
class TestConnection:

    def test_create_database_engine(self):
        db_connection_handle = DBConnectionHandler()
        engine = db_connection_handle.get_engine()
        assert engine is not None
