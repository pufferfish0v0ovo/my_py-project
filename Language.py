import urllib.request
import urllib.parse
import json
from datetime import datetime, timedelta

language = input("请输入编程语言: ")

date_30_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

params = {
    "q": f"language:{language} created:>{date_30_days_ago}",
    "sort": "stars",
    "order": "desc",
    "per_page": 10
}

url = (
    "https://api.github.com/search/repositories?"
    + urllib.parse.urlencode(params)
)

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    print(f"\n最近30天最热门的 {language} 项目:\n")

    for i, repo in enumerate(data["items"], start=1):
        print(f"{i}. {repo['full_name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Forks: {repo['forks_count']}")
        print(f"Description: {repo['description']}")
        print("-" * 50)

except Exception as e:
    print("发生错误：", e)