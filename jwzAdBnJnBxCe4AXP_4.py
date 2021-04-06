
def rearranged_difference(num):
  a=sorted(list(str(num)))
  return int(''.join(a[::-1]))-int(''.join(a))

