
def gimme_the_letters(spectrum):
  s = spectrum.split("-")
  res = []
  for k in range(ord(s[0]), ord(s[1])+1):
    res.append(chr(k))
  return "".join(res)

