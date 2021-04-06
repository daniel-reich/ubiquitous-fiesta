
def print_all_groups():
  res = []
  for x in range(1,7):
    for c in 'abcde':   
      res.append(str(x)+c)
  return ', '.join(res)

