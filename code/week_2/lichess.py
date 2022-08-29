from rich import print
import requests

LICHESS_API_PATH = "https://lichess.org/api/"


def get_user(user_ids):
    user_ids = ",".join(user_ids)
    url = f"{LICHESS_API_PATH}users/status?ids={user_ids}"
    data = list(requests.get(url))
    return data


user_ids = ["cross_online", "bombegranate"]
result = get_user(user_ids)
print(result)
