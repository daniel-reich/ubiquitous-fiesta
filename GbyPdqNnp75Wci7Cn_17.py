
def count_ones(num):
  return sum(x == '1' for x in str(bin(num))[2:])

