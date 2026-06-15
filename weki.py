import urllib.request
import urllib.parse
import json

keyword = input("Please input the keyword：")

# 第一步：搜索
search_url = (
    "https://en.wikipedia.org/w/api.php?"
    f"action=query&list=search&srsearch={urllib.parse.quote(keyword)}&format=json"
)

with urllib.request.urlopen(search_url) as response:
    data = json.loads(response.read().decode())

results = data["query"]["search"]

if not results:
    print("no solution")
    exit()

title = results[0]["title"]

print("find the list：", title)

# 第二步：获取简介
summary_url = (
    "https://en.wikipedia.org/w/api.php?"
    f"action=query&prop=extracts&exintro&explaintext&titles={urllib.parse.quote(title)}&format=json"
)

with urllib.request.urlopen(summary_url) as response:
    summary_data = json.loads(response.read().decode())

pages = summary_data["query"]["pages"]

for page in pages.values():
    print("\nintroduce：")
    print(page["extract"])