
def inverter(txt, t):
  txt = txt.split(" ")
  if t == "W":
    a = []
    for i in txt:
      a.append("".join(i[::-1]))
​
    return (" ".join(a)).capitalize()
​
  return (" ".join(txt[::-1])).capitalize()

