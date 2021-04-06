
def pig_latin_sentence(sentence):
  res = []
  for s in sentence.split():
    for i,c in enumerate(s):
      if c in 'aeiou':
        res.append((s[i:]+s[:i]+'ay') if i > 0 else s + 'way')
        break
  return ' '.join(res)

