class UserRegisterSpy:
    def __init__(self):
        self._find_attributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> dict:
        self._find_attributes["first_name"] = first_name
        self._find_attributes["last_name"] = last_name
        self._find_attributes["age"] = age

        return {
            "type": "users",
            "count": 1,
            "attributes": [self._find_attributes],
        }
