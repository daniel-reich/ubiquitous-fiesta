
def is_scalable(lst):
  return all(abs(int(lst[i]) - int(lst[i+1])) <= 5 for i in range(len(lst) - 1))

