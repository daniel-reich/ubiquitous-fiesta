
def twins(lst):
  S = sum(lst)
  for i in range(len(lst)):
    if S == 2*sum(lst[:i]):
      return i

