
def reverse_case(txt):
  revtxt = ''
  for i in range(len(txt)):
    if txt[i].isupper():
      revtxt += txt[i].lower()
    else:
      revtxt += txt[i].upper()
  return revtxt

