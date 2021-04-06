
def is_slidey(n):
  n = str(n)
  return all(abs(int(n[i]) - int(n[i+1])) == 1 for i in range(len(n) - 1))

