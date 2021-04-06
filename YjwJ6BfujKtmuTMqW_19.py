
def dice_game(scores):
  score_generator = (score for score in scores)
  players = ['p{}'.format(num) for num in range(1, 5)]
    
  while True:
    if len(players) == 1:
      return players[0]
    
    total_rolls = []
    first_rolls = []
    for player in players:
      roll = next(score_generator)
      total_rolls.append(sum(roll))
      first_rolls.append(roll[0])
​
    if total_rolls.count(min(total_rolls)) == 1:
      players.remove(players[total_rolls.index(min(total_rolls))])
    else:
      check2 = [first_rolls[total_index] if total == min(total_rolls) else 99 for total_index, total in enumerate(total_rolls)]
      print('check2', check2)
      if check2.count(min(check2)) == 1:
        players.remove(players[check2.index(min(check2))])

