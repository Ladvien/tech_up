import berserk
from rich import print

USERNAME = "cross_online"

client = berserk.Client()

result = client.games.export_by_player(
    USERNAME, max=200, evals=True, moves=True, opening=True
)

result = list(result)

for game in result:
    white = f"""White: {game["players"]["white"]["user"]["name"]}"""
    black = f"""Black: {game["players"]["white"]["user"]["name"]}"""
    moves = game["moves"]

    print("#################################")
    print(white)
    print(black)
    print(f"Moves: {moves}")
    print("#################################")
