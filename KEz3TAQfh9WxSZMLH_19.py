
def count_all(txt):
  letters, digits=0, 0
  for i in txt:
    if i.isalpha():
      letters +=1
    if i.isdigit():
      digits +=1
  return {"LETTERS": letters, "DIGITS": digits}

