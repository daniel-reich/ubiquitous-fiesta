
def join_digits(n):
  y = ""
  for x in range(1, n + 1):
    if x < 10:
      y += str(x) + "-"
    else:
      for z in str(x):
        y += z + "-"
  return y.rstrip("-")

