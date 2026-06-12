from .utils import find_user_by_id


class API:
    def __init__(self):
        self.data = {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"},
                {"id": 3, "name": "Charlie"}
            ]
        }

    def get_users(self):
        return self.data["users"]

    def get_user_by_id(self, user_id):
        return find_user_by_id(
            self.data["users"],
            user_id
        )