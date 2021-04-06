
def kaprekar(num, count=0):
  if num == 6174:
    return count;
  num = str(num).zfill(4)
  ascend = int(''.join(sorted(num)))
  descend = int(''.join(sorted(num, reverse=True)))
  return kaprekar(max(ascend, descend) - min(ascend, descend), count + 1)

