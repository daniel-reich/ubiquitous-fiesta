
def flip(txt, spec):
  new = []
  txt = txt.split()
  if spec == "word":
    for word in txt:
      new.append(word[::-1])
    return ' '.join(new)
  else:
    txt.reverse()
    return ' '.join(txt)

