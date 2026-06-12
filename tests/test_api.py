from projet_api import API


def test_get_users():
    api = API()

    users = api.get_users()

    assert len(users) == 3


def test_get_user_by_id():
    api = API()

    user = api.get_user_by_id(1)

    assert user["name"] == "Alice"