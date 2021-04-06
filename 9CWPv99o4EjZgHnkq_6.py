
def divide(lst, n):
  result = []
  current = []
  total = 0
  for item in lst:
    if total + item > n:
      result.append(current)
      current = [item]
      total = item
    else:
      current.append(item)
      total += item
  result.append(current)
  return result

