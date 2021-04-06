
def find_a_seat(n, lst):
  try:
    return next(i for i,l in enumerate(lst) if l <= (n/(len(lst)))/2) 
  except:
    return -1

