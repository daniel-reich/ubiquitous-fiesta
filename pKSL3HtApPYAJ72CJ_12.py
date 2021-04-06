
def name_shuffle(txt):
  txt = txt.split(" ")
  txt = txt[::-1]
  txt2 = []
  for word in txt:
    txt2.append(word)
  return " ".join(txt2)

