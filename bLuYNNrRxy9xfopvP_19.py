
from collections import Counter
def yahtzee_score_calc(lst):
  y_sum = lambda lst, n: lst.count(n) * n
​
  total = 0
  for throw, dice in enumerate(lst):
    ds = set(dice)
    ss = sorted(ds)
    if throw < 6:
      total += dice.count(throw + 1) * (throw + 1)
    elif throw < 8:
      if throw == 6 and total >= 63:
        total += 35
      total += sum(dice) if Counter(dice).most_common(1)[0][1] > throw - 4 else 0
    elif throw == 8:
      c = Counter(dice).most_common(3)
      total += 25 if len(c) == 2 and c[0][1] == 3 else 0
    elif throw == 9:
      total += 30 if ss in [[1,2,3,4], [2,3,4,5], [3,4,5,6], [1,2,3,4,5], [1,2,3,4,6], [2,3,4,5,6]] else 0
    elif throw == 10:
      total += 40 if ss == [1,2,3,4,5] or ss == [2,3,4,5,6] else 0
    elif throw == 11:
      total += 50 if len(ds) == 1 else 0
    else:
      total += sum(dice)
  return total

