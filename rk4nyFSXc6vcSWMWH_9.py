
def shared_digits(lst):
  return all(len(set(str(x)) & set(str(y))) > 0  for x,y in zip(lst[:-1],lst[1:]))

