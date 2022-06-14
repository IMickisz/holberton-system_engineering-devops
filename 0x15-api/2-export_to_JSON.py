#!/usr/bin/python3
"""Python script that export employee data information in json file"""


if __name__ == "__main__":
    from sys import argv
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = requests.get(url)
    user = api_url.json().get("username")
    user_id = api_url.json().get("id")
    to_do = requests.get("{}/todos".format(url))
    filename = "{}.json".format(argv[1])
    todo_list = []

    for value in to_do.json():
        data = {"task": value.get('title'),
                "completed": value.get('completed'),
                "username": user}
        todo_list.append(data)
        dico = {user_id: todo_list}
        object_json = json.dumps(dico)

    with open(filename, "w") as f:
        f.write(object_json)
