import requests
from pprint import pprint
result = requests.get("https://lichess.org/api")
print(result.status_code)

user = requests.get("https://lichess.org/api/user/cross_online")

pprint(user.json()["profile"]["bio"])
pprint(user.json()["createdAt"])
pprint(user.json()["playTime"]["total"])