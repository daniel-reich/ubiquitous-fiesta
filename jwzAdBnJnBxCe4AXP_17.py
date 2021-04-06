
def rearranged_difference(num):
  s = [i for i in str(num)]
  low = sorted(s)
  high = sorted(low, reverse = True)
  return int("".join(high)) - int("".join(low))

