
def missing_letter(txt):
  for foo in range(ord(txt[0]) , ord(txt[-1])):
      if chr(foo) not in txt:
        return chr(foo)
  return "No Missing Letter"

