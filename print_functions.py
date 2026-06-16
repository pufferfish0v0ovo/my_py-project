import json
import requests
import base64

# 输出与用户有关的=====================================

# 输出用户基本信息
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
    input("\nPress Enter to continue...")


def print_userrepos_info():
    with open("userrepos_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for repo in data:
        print(repo["name"], "-", repo["language"], "-", repo["description"])
        print("==============================")
    input("\nPress Enter to continue...")

def print_hot_projects():
    with open("hotprojects_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    projects = data["items"]
    print("=========== HOT PROJECTS ===========")
    for i, repo in enumerate(projects[:20], 1):
        print(
            f"{i}. "
            f"{repo['full_name']} "
            f"- Stars: {repo['stargazers_count']}"
        )
    choice = int(
        input("\nSelect repository:")
    )
    selected = projects[choice - 1]
    response = requests.get(selected["url"])
    repo_data = response.json()

    with open("repo_data.json", "w", encoding="utf-8") as f:
        json.dump(repo_data, f, indent=4)

    print_target_repos()

# 输出与仓库有关的============================================

# 输出某个仓库基本信息
def print_repo_basic_info():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("reponame", data.get("name", "UNKNOWN"))
    print("owner:", data.get("owner", {}).get("login", "UNKNOWN"))
    print("description:", data.get("description", "None"))
    print("language:", data.get("language", "None"))
    print("star", data.get("stargazers_count", 0))
    print("fork", data.get("forks_count", 0))
    print("open_issues", data.get("open_issues_count", 0))
    print("created_at", data.get("created_at", "None"))
    print("updated_at", data.get("updated_at", "None"))
    print("html_url", data.get("html_url", "None"))


def print_repo_README():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    username = data.get("owner", {}).get("login", "UNKNOWN")
    reponame = data.get("name", "UNKNOWN")
    url = f"https://api.github.com/repos/{username}/{reponame}/readme"
    response = requests.get(url)

    # print(response.status_code)
    # print(response.text)

    if response.status_code != 200:
        print("Something went wrong.")
        return
    readme_data = response.json()
    # readme = base64.b64decode(readme_data["content"])
    readme = base64.b64decode(readme_data["content"]).decode("utf-8")
    print("===================================")
    print(readme)
    input("\nPress Enter to continue...")


# 这个应该是需要传参
def print_repo_content():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    username = data.get("owner", {}).get("login", "UNKNOWN")
    reponame = data.get("name", "UNKNOWN")
    url = f"https://api.github.com/repos/{username}/{reponame}/contents"

    response = requests.get(url)
    if response.status_code != 200:
        print("Something went wrong.")
        return
    content = response.json()
    # i = 1
    # for item in content:
    #     if item["type"] == "file":
    #         print(i, "[FILE]", item["name"])
    #     else:
    #         print(i, "[DIR]", item["name"])
    #     i += 1
    history = []
    while True:
        for i, item in enumerate(content, 1):
            if item["type"] == "file":
                print(i, "[FILE]", item["name"])
            else:
                print(i, "[DIR]", item["name"])

        choice =input("Please enter your choice\n"
                      "You can enter 'exit', 'back', or a number:")
        if choice == "exit":
            break
        if choice == "back":
            if history:
                content = history.pop()
            else:
                print("Already at root directory.")
            continue

        choice = int(choice)
        selected = content[choice - 1]
        if selected["type"] == "file":
            url = f"https://api.github.com/repos/{username}/{reponame}/contents/{selected['path']}"
            response = requests.get(url)
            if response.status_code != 200:
                print("Something went wrong.")
                return
            file_data = response.json()
            file_content = base64.b64decode(file_data["content"]).decode("utf-8")
            print(file_content)
        else:
            history.append(content)
            url = f"https://api.github.com/repos/{username}/{reponame}/contents/{selected['path']}"
            response = requests.get(url)
            content = response.json()
        input("\nPress Enter to continue...")

def print_repo_issues():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if "owner" not in data:
        print("GitHub API limit exceeded.")
        return

    username = data["owner"]["login"]
    reponame = data["name"]
    url = f"https://api.github.com/repos/{username}/{reponame}/issues"
    response = requests.get(url)
    if response.status_code != 200:
        print("Something went wrong.")
        return
    issue_data = response.json()
    print("==================================")
    for i, issue in enumerate(issue_data, 1):
        print(i, "[ISSUE]", issue["title"])
    print("\npress Enter to continue...")
    while True:
        choice = input("Please enter your choice\n"
                       "You can enter 'exit' or a number:")
        if choice == "exit":
            return
        choice = int(choice)
        selected = issue_data[choice - 1]
        print("============================")
        print(selected["title"])
        print(selected["body"])
        print("\npress Enter to continue...")

# print_repo_issues()



def print_target_repos():
    print("===================================")
    # print(data[""])
    print_repo_basic_info()
    choose1 = input("If you want to view the README of this repository, enter Y or y. Otherwise, enter any other character.")
    if choose1.lower() == "y":
        print_repo_README()
    print_repo_content()
    choose2 = input("If you want to view the issues of this repository, enter Y or y. Otherwise, enter any other character.")
    if choose2.lower() == "y":
        print_repo_issues()
    choose3 = input("\nView repository owner? (Y/N): ")

    if choose3.lower() == "y":
        print_repo_owner()

# print_repo_README()


def print_repo_owner():
    with open("repo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    username = data["owner"]["login"]
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Something went wrong.")
        return

    user_data = response.json()
    with open("user_data.json", "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4)
    print_user_basic_info()

