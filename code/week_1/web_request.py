import requests

result = requests.get("https://en.wikipedia.org/wiki/Web_API")
print(result.status_code)
