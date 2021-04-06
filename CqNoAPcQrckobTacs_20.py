
def missing_letter(lst):
  x = ord(lst.pop(0))
  for i in lst:
    i = ord(i)
    if i == x + 1:
      x = i
    else:
      return chr(x + 1)

