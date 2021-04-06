
def is_smooth(txt):
  txt = txt.lower()
  lst = []
  for i in range(len(txt)):
    if txt[i] == " ":
      if txt[i - 1] == txt[i + 1]:
        lst.append(True)
      else:
        return False
  return all(lst)

