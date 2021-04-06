
def retrieve(txt):
  return [i for i in txt[:-1].lower().split() if i[0] in 'aeiou']

