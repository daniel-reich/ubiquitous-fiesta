
def coconut_translator(txt):
  x = "stunococ"
  lst = []
  for c in txt:
    b = ord(c)
    s = ""
    for i in range(8):
      s = (x[i].upper() if b >> i & 1 else x[i]) + s
    lst.append(s)
  return " ".join(lst)

