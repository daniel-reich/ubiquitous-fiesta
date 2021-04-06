
def join_digits(n):
  c = ""
  for i in range(1,n+1):
    c+= str(i)
  return "-".join(c)

