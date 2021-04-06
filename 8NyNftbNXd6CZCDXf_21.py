
def get_coin_balances(lst1, lst2):
  commands = zip(lst1, lst2)
  green = red = 3
  for command in commands:
    green_action, red_action = command
    if [green_action, red_action] == ["share", "share"]:
      green += 2
      red += 2
    elif [green_action, red_action] == ["steal", "steal"]:
      continue
    elif [green_action, red_action] == ["share", "steal"]:
      green -= 1
      red += 3
    else:
      green += 3
      red -= 1
  return [green, red]

