import requests
import csv
import json
import print_functions
import base64
import urllib.parse
from print_functions import *

# 查找用户信息
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

#查找一个用户的所有仓库信息
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

# 查找指定用户的指定仓库
def get_repos_user_info():
    username = input("Username: ")
    reposname = input("Repository name: ")
    url = f"https://api.github.com/repos/{username}/{reposname}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("repo_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print_target_repos()
    else:
        print("Something went wrong.")

# 查找仓库菜单
def get_repos_info():
    print("**********************************************************")
    print("Now you can search for repositories using two methods:")
    print("1. Search all repositories of a user")
    print("2. Search by username and repository name")
    print("**********************************************************")

    choose = (int(input("Please enter your choice: ")))
    if choose == 1:
        get_userrepos_info()
    elif choose == 2:
        get_repos_user_info()

    else:
        print("Invalid choice.")


def search_projects_by_keyword():
    keyword = input("Please input keyword: ")
    keyword = urllib.parse.quote(keyword)
    url = (
        "https://api.github.com/search/repositories?"
        f"q={keyword}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        print("Something went wrong.")
        return
    data = response.json()
    repos = data["items"][:10]
    print("\nSearch Result:\n")
    for i, repo in enumerate(repos, 1):
        print(
            f"{i}. "
            f"{repo['full_name']} "
            f"- stars: {repo['stargazers_count']}"
        )
    choice = int(
        input("\nSelect the number you want to search:")
    )
    selected = repos[choice - 1]
    repo_response = requests.get(selected["url"])
    repo_data = repo_response.json()
    with open("repo_data.json", "w", encoding="utf-8") as f:
        json.dump(repo_data, f, indent=4)

    print_target_repos()


def get_all_hot_projects():
    url = (
        "https://api.github.com/search/repositories?"
        "q=stars:>50000&sort=stars&order=desc"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open("hotprojects_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print_hot_projects()

    else:
        print("Something went wrong.")

def get_hot_projects_by_language():

    language = input(
        "Please input a programming language: "
    )

    url = (
        "https://api.github.com/search/repositories?"
        f"q=language:{urllib.parse.quote(language)}"
        "&sort=stars"
        "&order=desc"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Something went wrong.")
        return

    data = response.json()

    with open(
        "hotprojects_data.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(data, f, indent=4)

    print_hot_projects()

# 查找热门项目
def get_hot_projects():

    print("=========== HOT PROJECT MENU ===========")
    print("1. All Hot Projects")
    print("2. Hot Projects By Language")
    print("========================================")

    choice = input("Please enter your choice: ")

    if choice == "1":
        get_all_hot_projects()

    elif choice == "2":
        get_hot_projects_by_language()

    else:
        print("Invalid choice.")