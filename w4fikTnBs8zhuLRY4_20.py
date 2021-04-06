
def rep_set(n):
  result = []
  for i in range(n):
    result.append([x for x in result])
  return result

