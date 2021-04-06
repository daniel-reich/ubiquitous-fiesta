
def uncensor(txt, vowels):
  i = 0
  encode = ""
  for letter in txt:
    if letter == "*":
      encode += vowels[i]
      i += 1
    else: 
      encode += letter 
  return encode

