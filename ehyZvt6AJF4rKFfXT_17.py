
def uncensor(txt, vowels):
  for i in range(len(vowels)):
      txt=txt.replace('*',vowels[i],1)
  return txt

