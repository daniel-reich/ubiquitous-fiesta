
def shared_letters(txt1, txt2):
  set1 = set(txt1)
  set2 = set(txt2)
  return len(set1 & set2)

