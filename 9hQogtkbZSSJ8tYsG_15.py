
def reverse(txt):
  lst = ""
  for i in txt:
    if i.isupper():
      lst += i.lower()
    else:
      lst += i.upper()
  return lst[::-1]

