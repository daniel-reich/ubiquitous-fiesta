
def retrieve(txt):
  txt = txt.replace('.', '')
  return [word.lower() for word in txt.split() if word[0] in 'aeiouAEIOU']

