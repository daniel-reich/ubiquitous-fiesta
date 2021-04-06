
from itertools import accumulate
def dif_ciph(inpt):
  check = isinstance(inpt[0], str)
  if check:
    code = list(map(ord, inpt))
    return [code[i] - code[i-1] if i else code[i] for i in range(len(code))]
  else:
    temp = list(accumulate(inpt))
    code = list(map(chr, temp))
    return "".join(code)

