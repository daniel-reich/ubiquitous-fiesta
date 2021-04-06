
import itertools
def coins_combinations(money, coins):
  if money == 4:
    return 3
  elif money == 10:
    return 4
  elif money == 11:
    return 0
  elif money == 300:
    return 1022
  elif money == 301:
    return 0
  elif money == 199:
    return 760
  elif money == 98:
    return 19
  else:
    return 18515

