
def count_digits(lst, t):
  lst=[list(str(i)) for i in lst]
  if t=="odd": lst=[sum([1 for i in y if int(i)%2]) for y in lst]
  else: lst=[sum([1 for i in y if not int(i)%2]) for y in lst]
  return lst

