
def missing_letter(txt):
  for i in range(0,len(txt) - 1):
    if ord(txt[i]) + 1 != ord(txt[i + 1]):
          return chr(ord(txt[i]) + 1)
  return "No Missing Letter"

