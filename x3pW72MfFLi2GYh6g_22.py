
def is_scalable(lst):
  return all(abs(lst[i]-lst[i+1]) <= 5 for i in range(len(lst)-1))

