
def uncensor(txt, vowels):
  vowels = iter(vowels)
  return ''.join(next(vowels) if i == '*' else i for i in txt)

