import berserk
from rich import print

USERNAME = "cross_online"

client = berserk.Client()

# Get realtime status
print(client.users.get_realtime_statuses(USERNAME))

# Get public adata
print(client.users.get_public_data(USERNAME))
