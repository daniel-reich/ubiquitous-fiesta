
def diving_minigame(lst):
  b = 10
​
  for n in lst:
    if n < 0:
      b -= 2
    else:
      b = 10 if b > 6 else b + 4
​
    if b <= 0:
      return False
​
  return b >= 0

