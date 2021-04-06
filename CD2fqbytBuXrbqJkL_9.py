
def can_build(txt1, txt2):
  letters = list(txt2)
  for ch in txt1:
    if ch != ' ':
      if ch in letters:
        letters.remove(ch)
      else:
        return False
  return True

