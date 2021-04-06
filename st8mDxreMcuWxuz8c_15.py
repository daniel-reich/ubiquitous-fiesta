
def pentagonal(num):
  dots = 1
  for i in range(2,num+1):
    dots += 5 + 5*(i-2)
  return dots

