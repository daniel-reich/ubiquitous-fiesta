
def difference_two(lst):
  lst.sort()
  twos = []
  for i in range(len(lst) - 2):
    if lst[i + 2] - lst[i] == 2:
      twos.append([lst[i], lst[i + 2]])
    elif lst[i + 1] - lst[i] == 2:
      twos.append([lst[i], lst[i + 1]])
  return twos

