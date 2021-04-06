
def hangman(phrase, lst):
  txt=""
  for i in phrase:
    if i.isalpha():
      if i.lower() in lst or i.upper() in lst:
        txt+=i
      else:
        txt+="-"
    else:
      txt+=i
  return txt

