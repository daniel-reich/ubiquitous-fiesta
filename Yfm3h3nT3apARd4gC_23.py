
def rolls(lst):
  total = lst[0]
  prev_roll = lst[0]
  for i in range(1, len(lst)):
    total += 0 if prev_roll == 1 else 2 * lst[i] if prev_roll == 6 else lst[i]
    prev_roll = lst[i]
  return total

