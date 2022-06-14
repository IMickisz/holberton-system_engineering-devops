#!/usr/bin/python3
"""Python script that, using the REST API, for a given enmployee ID, returns
information about his/her TODO list progress"""

if __name__ == "__main__":
    import requests
    from sys import argv


    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = requests.get(url)
    user = api_url.json().get("name")

    to_do = requests.get("{}/todos".format(url))
    total_tasks = len(to_do.json())
    list_tasks = []

    for value in to_do.json():
        if value.get("completed") is True:
            list_tasks.append(value.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user, len(list_tasks), total_tasks))
    for i in list_tasks:
        print("\t {}".format(i))
