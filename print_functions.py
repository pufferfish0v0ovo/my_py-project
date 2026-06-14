import json
import requests
import base64

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

def print_repo_basic_info():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("reponame", data["name"])
    print("owner:", data["owner"]["login"])
    print("description:", data["description"])
    print("language:", data["language"])
    print("star", data["stargazers_count"])
    print("fork", data["forks_count"])
    print("open_issues", data["open_issues_count"])
    print("created_at", data["created_at"])
    print("updated_at", data["updated_at"])
    print("html_url", data["html_url"])


def print_repo_README():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    username = data["owner"]["login"]
    reponame = data["name"]
    url = f"https://api.github.com/repos/{username}/{reponame}/readme"
    response = requests.get(url)
    if response.status_code != 200:
        print("Something went wrong.")
        return
    readme_data = response.json()
    # readme = base64.b64decode(readme_data["content"])
    readme = base64.b64decode(readme_data["content"]).decode("utf-8")
    print("===================================")
    print(readme)

# 这个应该是需要传参
def print_repo_content():
    print("22222222222")

def print_repo_tree():
    print("33333333333")

def print_repo_issues():
    print("44444444444")

def print_target_repos():
    with open("repos_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("===================================")
    # print(data[""])
    print_repo_basic_info()
    choose1 = input("If you want to view the README of this repository, enter Y or y. Otherwise, enter any other character.")
    if choose1.lower() == "y":
        print_repo_README()
    print_repo_content()




