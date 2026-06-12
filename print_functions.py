import json
import requests

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

def print_userrepos_info():
    with open("userrepos_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for repo in data:
        print(repo["name"], "-", repo["language"], "-", repo["description"])
        print("==============================")


def print_target_repos():
    with open("target_repos_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("===================================")
    # print(data[""])





