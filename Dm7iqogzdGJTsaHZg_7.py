
def retrieve(txt):
  l=[i.lower() for i in txt.split() if i[0] in 'aeiouAEIOU']
  return [i if i[-1].isalpha() else i[:-1] for i in l]

