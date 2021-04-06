
def is_scalable(lst):
  return all(5>=abs(lst[i]-lst[i+1]) for i in range(len(lst)-1))

