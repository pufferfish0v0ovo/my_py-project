import json

import requests

url = "https://api.github.com/users/pufferfish0v0ovo"

response = requests.get(url)
# print(response.json())

data = requests.get(url).json()

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



# print("用户名", data["login"])
# print("粉丝数",data["followers"])
# print("公开仓库", data["public_repos"])

# import requests
#
# url = "https://api.github.com/rate_limit"
#
# data = requests.get(url).json()
#
# print(data)