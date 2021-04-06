
def dif_ciph(inpt):
  if type(inpt) == str:
    out = [ord(inpt[0])]
    for i in range(1, len(inpt)):
      out.append(ord(inpt[i]) - ord(inpt[i-1]))
  
  if type(inpt) == list:
    out = str(chr(inpt[0]))
    for i in range(1, len(inpt)):
      out += chr(inpt[i] + ord(out[i-1]))
  
  return out

