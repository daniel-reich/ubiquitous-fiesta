
def dif_ciph(inpt):
  if type(inpt) is str:
    return [ord(inpt[0])] + [ord(b) - ord(a) for a,b in zip(inpt,inpt[1:])]
  else:
    for i in range(1, len(inpt)):
      inpt[i] += inpt[i-1]
    return ''.join(chr(code) for code in inpt)

