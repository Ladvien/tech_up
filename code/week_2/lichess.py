from rich import print
import requests

##############
# Parameters
##############
LICHESS_ID = "Cross_online"

##############
# Constants
##############
LICHESS_API_PATH = "https://lichess.org/api/"
ENDPOINT = "users/status"

RESOURCE_PATH = f"{LICHESS_API_PATH}{ENDPOINT}"
REQUEST_URL = f"{RESOURCE_PATH}?ids={LICHESS_ID}"

##############
# Request
##############
result = requests.get(REQUEST_URL)
data = result.json()

##############
# Get "name"
##############
first_user = data[0]
user_name = first_user["name"]
print(user_name)