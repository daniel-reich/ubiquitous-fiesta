
def rolls(lst):
  x = 0
  for n in range(1, len(lst)):
    if lst[-n - 1] == 1:
      x += 0
    elif lst[-n - 1] == 6:
      x += lst[-n] * 2
    else:
      x += lst[-n]
  return x + lst[0]

