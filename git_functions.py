import requests
import csv
import json

def print_user_basic_info():
    with open("user_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("=====================================")
    print("Username:", data["login"])
    print("name:", data["name"])
    print("Biography:", data["bio"])
    print("email:", data["email"])
    print("public repos:", data["public_repos"])
    print("public gists:", data["public_gists"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("=====================================")
    print("If you would like to view their GitHub profile in more detail, you can click the link below.")
    print(data["html_url"])




def get_user_info():
    print("You can now search for a user by entering their username.")
    user_username = input("Username: ")
    url = f"https://api.github.com/users/{user_username}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("user_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    else:
        print("Something went wrong.")
    print("\n")
    print_user_basic_info()
    # print("")


def get_repos_info():



def get__info():
    print("You can now search for a user by entering their username.")
