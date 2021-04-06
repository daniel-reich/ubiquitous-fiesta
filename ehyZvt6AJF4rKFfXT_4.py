
def uncensor(txt, vowels):
  v=list(vowels)
  return ''.join(v.pop(0) if i=="*" else i for i in txt)

