
def accum(txt):
  Repeater = 1
  Chapter = ""
  for Char in txt.lower():
    if Repeater == 1:
      Chapter+=Char.upper()+"-"
    else:
      Chapter+=Char.upper()
      Chapter+=Char*(Repeater-1)+"-"
    Repeater+=1
  NewChapter = list(Chapter)
  NewChapter.pop()
  return "".join(NewChapter)

