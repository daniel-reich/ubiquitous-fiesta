
def persistence(num):
  pcount = 0  # counting the p from 0
  while num >= 10:
    y = num  # temp copy of num
    z = 1  # z holds the value of y as being broken down and multplied
    while (y != 0):
      z = z * (y % 10)  # stripping last number and mult by last z value
      y = y // 10  # integer division, dropping off the last digit
    num = z
    pcount += 1
  return pcount

