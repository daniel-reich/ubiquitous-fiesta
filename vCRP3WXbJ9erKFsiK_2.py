
def dif_ciph(inpt):
  if type(inpt)==str:
    return [ord(inpt[0])]+[ord(inpt[i])-ord(inpt[i-1]) for i in range(1,len(inpt))]
  return ''.join([chr(sum(inpt[:i+1])) for i in range(len(inpt))])

