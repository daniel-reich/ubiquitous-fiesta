
def uncensor(txt, vowels):
  count = 0
  txt = list(txt)
  for i in range(len(txt)):
    if txt[i] == "*":
      txt[i] = vowels[count]
      count += 1
  return "".join(txt)

