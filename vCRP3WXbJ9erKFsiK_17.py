
def encode(txt):
  return [ord(txt[0])] + [ ord(cur) - ord(last) for last, cur in zip(txt, txt[1:])]
​
def decode(code):
  cur = 0
  out = []
  for delta in code:
    cur += delta
    out.append(chr(cur))
  return "".join(out)
  
def dif_ciph(inpt):
  if isinstance(inpt, str):
    return encode(inpt)
  else:
    return decode(inpt)

