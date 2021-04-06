
def rearranged_difference(num):
  digits = ''.join(sorted(str(num)))
  return int(digits[::-1]) - int(digits)

