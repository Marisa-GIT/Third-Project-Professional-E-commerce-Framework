
import json 

class TestDataManager:

    @staticmethod
    def read_users():
        with open("data/users.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_user(user_type):
        return TestDataManager.read_users()[user_type]