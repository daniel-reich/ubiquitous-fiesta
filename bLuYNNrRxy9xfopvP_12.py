
def yahtzee_score_calc(lst):
  def score(turn):
    if turn <= 6:
      return turn * lst[turn-1].count(turn)
    elif turn < 9 and any(list(map(lambda x: lst[turn-1].count(x) >= turn - 4,set(lst[turn-1])))):
      return sum(lst[turn-1])
    elif turn == 9 and len(set(lst[8])) == 2 and any(list(map(lambda x: lst[8].count(x) == 2, set(lst[8])))):
      return 25
    elif turn == 10:
      if sorted(lst[9])[:-1] == list(range(sorted(lst[9])[0],sorted(lst[9])[0]+4)):
        return 30
      elif sorted(lst[9])[1::] == list(range(sorted(lst[9])[1],sorted(lst[9])[1]+4)):
        return 30
      else:
        return 0
    elif turn == 11:
      return 40 if sorted(lst[10]) == list(range(sorted(lst[10])[0],sorted(lst[10])[0]+5)) else 0 
    elif turn == 12:  
      return 50 if len(set(lst[11])) == 1 else 0
    elif turn == 13:
      return sum(lst[12])
    else:
      return 0
  for i in range(1,14):
    print(score(i))
  total = sum(list(map(lambda x: score(x+1),range(0,13))))
  if sum(list(map(lambda x: score(x+1),range(0,6)))) >= 63:
    total += 35
  return total

