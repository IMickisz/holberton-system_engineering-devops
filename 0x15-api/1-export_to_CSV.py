#!/usr/bin/python3
"""Python script that export employee data information in csv file"""


if __name__ == "__main__":
    from sys import argv
    import requests
    import csv

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = requests.get(url)
    user = api_url.json().get("username")
    user_id = api_url.json().get("id")
    to_do = requests.get("{}/todos".format(url))
    filename = "{}.csv".format(argv[1])

    with open(filename, "w", encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)

        for value in to_do.json():
            data = [user_id, user, value.get('completed'),
                    value.get('title')]
            writer.writerow(data)
