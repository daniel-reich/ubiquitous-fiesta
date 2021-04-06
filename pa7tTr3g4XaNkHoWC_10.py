
def pig_latin_sentence(s):
  fin = []
  for w in s.split():
    vpos = min(w.index(a) for a in w if a in 'aeiou')
    if not vpos:
       fin.append(w+'way')
    else:
      fin.append(w[vpos:]+w[:vpos]+'ay')
  return ' '.join(fin)

