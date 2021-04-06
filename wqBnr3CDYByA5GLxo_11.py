
def unravel(txt):
  poss = [""]
  while txt:
    if txt[0] != "[":
      if "]" not in txt:
        add, txt = txt, ""
      else:
        r = txt.index("[")
        add, txt = txt[:r], txt[r:]
      poss = [p+add for p in poss]
    else:
      r = txt.index("]")
      add, txt = txt[1:r], txt[r+1:]
      poss = [p+a for p in poss for a in add.split("|")]
  return sorted(poss)

