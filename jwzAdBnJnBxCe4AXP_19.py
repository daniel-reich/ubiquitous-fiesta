
def rearranged_difference(num):
  big = "".join(sorted(str(num), reverse=True))
  small = "".join(sorted(str(num)))
  return int(big)-int(small)

