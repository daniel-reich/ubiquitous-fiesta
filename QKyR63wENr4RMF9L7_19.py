
def tweak_letters(txt, lst):
  l = [ord(i)+j for i,j in zip(txt,lst)]
  res = lambda l: "".join(chr(i+26) if i<97 else chr(i-26) if i>122 else chr(i) for i in l)
  return res(l)

