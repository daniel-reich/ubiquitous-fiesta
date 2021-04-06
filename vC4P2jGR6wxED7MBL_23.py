
def larger_than_right(lst):
  result = []
  for x in range(len(lst)):
    for y in range(x + 1, len(lst)):
      if lst[x] <= lst[y]:
        break
      if y == len(lst) - 1:
        result.append(lst[x])
  result.append(lst[-1])
  return result

