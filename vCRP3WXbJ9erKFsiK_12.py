
def dif_ciph(inpt):
  vec = []
  cuv = ''
  nr = inpt[0]
  if type(vec) is type(inpt):
    cuv = chr(inpt[0])
    for i in range(1,len(inpt)):
      nr += inpt[i]
      cuv += chr(nr)
    return cuv
  else:
    vec.append(ord(inpt[0]))
    for i in range(1,len(inpt)):
      vec.append(ord(inpt[i]) - ord(inpt[i - 1]))
    return vec

