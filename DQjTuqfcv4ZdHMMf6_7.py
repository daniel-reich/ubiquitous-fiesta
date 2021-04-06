
def kaprekar(num, steps = 0):
  if num == 6174:
    return steps
  if num < 1000:
    num = list(str(num))+(['0']*(4-len(str(num))))
  else:
    num = list(str(num))
  num.sort()
  return kaprekar(int(''.join(num[::-1])) - int(''.join(num)),steps+1)

