
def uncensor(txt, vowels):
  n = 0
  for i, char in enumerate(txt):
    if char == "*":
      txt = txt[0:i] + vowels[n] + txt[i+1:len(txt)]
      n += 1
  return txt

