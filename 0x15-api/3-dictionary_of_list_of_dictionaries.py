#!/usr/bin/python3
"""Python script that export employee data information in json file"""


if __name__ == "__main__":
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/users/"
    api_url = requests.get(url)
    filename = "todo_all_employees.json"
    dico = {}

    for values in api_url.json():
        user = values.get("username")
        user_id = values.get("id")
        to_do = requests.get("{}{}/todos".format(url, user_id))
        todo_list = []

        for value in to_do.json():
            data = {"task": value.get('title'),
                    "completed": value.get('completed'),
                    "username": user}
            todo_list.append(data)
        dico[user_id] = todo_list
        object_json = json.dumps(dico)

    with open(filename, "w") as f:
        f.write(object_json)
