
def count(deck):
  result = []
  if deck == []:
    return 0
  else:
    for item in deck:
      if item in [2,3,4,5,6]:
        result.append(1)
      elif item in [7,8,9]:
        result.append(0)
      else:
        result.append(-1)
  ans = sum(result)
  return ans

