
def decode(txt):
  lol = "defghijklmnopqrstuvwxyzabc"
  lst = []
  ok = 0
  for x in txt:
    print(x)
    if x == " ":
      lst.append(5)
      ok += 1
    if x == "R":
      lst.append(10)
      ok += 1
    if ok >= 1:
      ok = 0
    elif lol.index(x) + 1 <= 10:
      lst.append(lol.index(x) + 1)
    elif lol.index(x) + 1 <= 20:
      lst.append(lol.index(x) + 1 - 10 + 1)
    elif lol.index(x) + 1 <= 23:
      lst.append(lol.index(x) + 1 - 20 + 2)
    else:
      lst.append(lol.index(x) + 1 - 10 + 2)
  print(lst)
  return lst

