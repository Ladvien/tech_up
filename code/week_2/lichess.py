from rich import print
import requests

LICHESS_ID = "Cross_online"
LICHESS_API_PATH = "https://lichess.org/api/"


def get_user(user_id):
    url = f"{LICHESS_API_PATH}users/status?ids={user_id}"
    data = requests.get(url)
    return data


result = get_user(LICHESS_ID)
data = result.json()

first_user = data[0]
user_name = first_user["name"]
print(user_name)

result2 = get_user("bombegranate")
print(list(result2))
