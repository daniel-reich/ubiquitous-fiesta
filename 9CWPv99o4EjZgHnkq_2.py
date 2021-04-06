
def divide(lst, n):
  res = []
  accumulated = 0
  buffer = []
  for e in lst:
    if e > n:
      raise Exception('No possible solution')
    accumulated += e
    if (accumulated > n):
      res.append(buffer)
      accumulated = e
      buffer = [e]
    else:
      buffer.append(e)
  res.append(buffer)
  return res

