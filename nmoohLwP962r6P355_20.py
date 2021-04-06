
def straight_digital(n):
  x = str(abs(n))
  lst = [int(x[d])-int(x[d-1]) for d in range(1, len(x))]
  if len(lst)==1 or len(set(lst))!=1 or n<0:
    return "Not Straight"
  elif len(set(x))==1:
    return "Trivial Straight"
  else:
    return lst[0]

