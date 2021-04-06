
def possible_path(lst):
  is_possible = True
  dict_possible = {3: [4], 4: [3, 'H'], 'H': [2, 4], 1: [2], 2: [1,'H']}
  for i in range(len(lst) - 1):
    if lst[i + 1] not in dict_possible[lst[i]]:
      is_possible = False
  return is_possible

