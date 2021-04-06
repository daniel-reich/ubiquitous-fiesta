
def replace_vowels(txt, ch):
  out = ""
  for i in txt:
    if i in "aeiouAEIOU":
      out += ch
    else:
      out += i
  return out

