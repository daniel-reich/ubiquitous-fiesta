
def shared_letters(txt1, txt2):
  res = ""
  for i in txt1:
    if i in txt2 and not i in res:
      res += i
  return len(res)

