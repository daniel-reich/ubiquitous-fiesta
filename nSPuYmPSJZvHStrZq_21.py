
def oddeven(lst):
  return sum(1 if i%2 else -1 for i in lst) >= 0

