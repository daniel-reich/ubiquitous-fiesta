
def pentagonal(num):
  dots = 1
  for i in range(1, num):
    dots += 5 * i
  return dots

