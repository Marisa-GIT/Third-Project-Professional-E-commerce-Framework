import json

def read_users():

    with open(
        "data/users.json",
        "r"
    ) as file:
        return json.load(file)