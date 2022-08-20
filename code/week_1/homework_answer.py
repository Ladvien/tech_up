from rich import print
import requests

##############
# Parameters
##############
USER_NAME = "mrbasso"

##############
# Constants
##############
LICHESS_API_PATH = "https://lichess.org/api"
ENDPOINT = "/user"

RESOURCE_PATH = f"{LICHESS_API_PATH}{ENDPOINT}"
REQUEST_URL = f"{RESOURCE_PATH}/{USER_NAME}"

##############
# Request
##############
print(REQUEST_URL)
result = requests.get(REQUEST_URL)
print(result.json())
# data = result.json()
