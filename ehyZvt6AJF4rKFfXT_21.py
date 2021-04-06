
def uncensor(txt, vowels):
  string = ""
  for i in txt:
    if i == "*":
      string += vowels[0]
      vowels = vowels[1:]
      continue
    string += i
  return string

