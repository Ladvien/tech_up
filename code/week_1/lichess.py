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
print(result.json())