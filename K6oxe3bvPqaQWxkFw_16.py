
def join_digits(n):
  t = ""
  for i in range(1,n+1):
    t += str(i)
  return "-".join(list(t))

