
def calculate_score(games):
  player = [0,0]
  names = ["Abigail","Benson"]
  for game in games:
    if "R" in game and "S" in game:
      player[game.index("R")] += 1
    if "R" in game and "P" in game:
      player[game.index("P")] += 1
    if "P" in game and "S" in game:
      player[game.index("S")] += 1
​
  return "Tie" if len(set(player)) == 1 else names[player.index(max(player))]

