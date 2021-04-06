
def dif_ciph(inpt):
  if isinstance(inpt, str):
    return [ord(inpt[i]) if i==0 else ord(inpt[i])-ord(inpt[i-1])for i in range(len(inpt))]
  else:
    return "".join([chr(inpt[i])if i==0 else chr(sum(inpt[:i+1])) for i in range(len(inpt)) ])

