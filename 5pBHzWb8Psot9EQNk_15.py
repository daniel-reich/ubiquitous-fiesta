
def simple_encoder(s):
  s = s.lower()
  box = []
  for i in range(len(s)):
    if s.count(s[i])==1:
      box.append("[")
    else:
      box.append("]")
  return "".join(box)

