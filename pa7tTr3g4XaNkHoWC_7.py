
def pig_latin_sentence(sentence):
  v = 'aieuo' ; L = []
  for w in sentence.split():
    if w[0] in v: L.append(w+'way')
    else:
      for i in w:
        if i in v:
          L.append(w[w.index(i):]+w[:w.index(i)]+'ay')
          break
  return " ".join(L)

