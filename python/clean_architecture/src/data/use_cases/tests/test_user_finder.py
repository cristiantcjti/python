from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_finder import UserFinder


def test_find():
    first_name = "NameTest"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes["first_name"] == first_name
    assert response["type"] == "users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []
