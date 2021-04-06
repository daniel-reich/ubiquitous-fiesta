
def ways_to_climb(n):
  if n < 1:
    return 1
  else:
    a, b = 1, 1
    for i in range(1,n):
      a, b = b, a + b
    return b

