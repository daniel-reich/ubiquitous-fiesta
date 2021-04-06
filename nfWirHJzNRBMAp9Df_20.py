
def hamming_distance(txt1, txt2):
  lista = []
  for i in txt2:
    if i != txt1[txt2.index(i)]:
      lista.append(1)
  return sum(lista)

