
def mystery_func(lst, n):
  temp = []
  for item in lst:
    temp.append(item%n)
  return temp

