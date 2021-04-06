
def kaprekar(num, cnt=0):
  if num == 6174:
    return cnt
  else:
    desc = int(''.join(sorted(list(str(num)), reverse=True)))
    aecs = int(''.join(sorted(list(str(num)))))
    value = desc-aecs
    while len(list(str(value)))<4:
      value *= 10
    return kaprekar(num=(value), cnt=cnt+1)

