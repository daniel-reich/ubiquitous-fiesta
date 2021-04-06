
def rolls(lst):
  score = 0
  for index, num in enumerate(lst):
    if index - 1 < 0:
      score += num
      continue
    if lst[index - 1] == 1:
      continue
    elif lst[index - 1] == 6:
      score += 2 * num
    else:
      score += num
  return score

