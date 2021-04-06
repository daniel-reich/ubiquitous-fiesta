
def who_goes_free(n, k):
  circle = list(range(n))
  i = 0
  while (len(circle) != 1):
    i += (k - 1)
    while (i >= len(circle)):
      i -= len(circle)
    circle.pop(i)
  return int(circle[0])

