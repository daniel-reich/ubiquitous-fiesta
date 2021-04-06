
def shared_letters(txt1, txt2):
  return sum(a in txt2 for a in set(txt1))

