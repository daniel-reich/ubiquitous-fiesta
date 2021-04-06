
def dif_ciph(inpt):
  if type(inpt)==str:
    return [ord(inpt[0])] + [ord(b)-ord(a) for a,b in zip(inpt, inpt[1:])]
  else:
    return ''.join([chr(sum(inpt[:x+1])) for x in range(len(inpt))])

