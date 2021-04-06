
def retrieve(txt):
  return [i.lower() for i in txt[:-1].split() if i[0] in 'aeiouAEIOU']

