
import itertools
def coins_div(lst):
  each = sum(lst)//3
  for i in list(itertools.permutations(lst)):
    total = 0
    gained = 0
    for j in i:
      total += j
      if total == each:
        total = 0
        gained += 1
        if gained == 3:
          return True
      elif total > each:
        break
  return False

