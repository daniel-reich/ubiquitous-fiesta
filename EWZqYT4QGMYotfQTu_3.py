
from string import ascii_lowercase as a
def tap_code(text):
  l = a.replace("k","")
  dot = lambda c: " ".join("."*x for x in c)
  enc = {x: tuple(map(sum,zip((1,1), divmod(l.index(x),5)))) for x in l}
  dec = {dot(v):k for k,v in enc.items()}
  enc.update({"k": (1,3)})
  if text.startswith("."):
    code = text.split()
    z = zip(code[::2], code[1::2])
    return "".join(dec.get(x) for x in (" ".join(y) for y in z))
  else:
    return " ".join(dot(enc.get(c)) for c in text)

