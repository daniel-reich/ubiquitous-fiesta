
def concat(*args):
  result = []
  for i in args:
    for j in i:
      result.append(j)
  return result

