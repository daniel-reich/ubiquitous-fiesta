
def rearranged_difference(num):
  n = ''.join(sorted(str(num)))
  return int(n[::-1]) - int(n)

