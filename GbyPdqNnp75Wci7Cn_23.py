
def count_ones(num):
  string="{0:b}".format(num)
  return sum([int(x) for x in string])

