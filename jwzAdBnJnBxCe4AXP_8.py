
def rearranged_difference(num):
  l1 = list(str(num))
  l1.sort()
  return int(''.join(l1[::-1]))- int(''.join(l1))

