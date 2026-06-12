import requests
import csv
import json
import print_functions
from print_functions import *

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


def get_userrepos_info():
    username = input("Username: ")
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("userrepos_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("\n")
        print_userrepos_info()

    else:
        print("Something went wrong.")


def get_repos_user_info():
    username = input("Username: ")
    reposname = input("Repository name: ")
    url = f"https://api.github.com/repos/{username}/{reposname}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("repos_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print_target_repos()
    else:
        print("Something went wrong.")


def get_repos_info():
    print("**********************************************************")
    print("Now you can search for repositories using two methods:")
    print("1. Search all repositories of a user")
    print("2. Search by username and repository name")
    print("3. Search by repository name only")
    print("**********************************************************")

    choose = (int(input("Please enter your choice: ")))
    if choose == 1:
        get_userrepos_info()
    elif choose == 2:
        get_repos_user_info()
    elif choose == 3:
        print("33333333333")
    else:
        print("Invalid choice.")

