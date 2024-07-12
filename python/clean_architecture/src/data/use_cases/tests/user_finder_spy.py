class UserFinderSpy:
    def __init__(self):
        self._find_attributes = {}

    def find(self, first_name: str) -> dict:
        self._find_attributes["first_name"] = first_name

        return {
            "type": "users",
            "count": 1,
            "attributes": [{"first_name": "John", "age": 25}],
        }
