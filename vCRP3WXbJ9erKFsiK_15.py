
def dif_ciph(inpt):
  if type(inpt) == str:
    return [ord(inpt[0])] + [ord(inpt[i])-ord(inpt[i-1]) for i in range(1,len(inpt))]
  else:
    return "".join([chr(inpt[0])]+[chr(inpt[i]+sum(inpt[:i])) for i in range(1,len(inpt))])

