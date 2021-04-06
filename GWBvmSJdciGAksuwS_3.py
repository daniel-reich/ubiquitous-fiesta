
def find_letters(word):
  lista = []
  for i in word:
    if word.count(i) > 1:
      word.replace(i,"")
    else:
      lista.append(i)
  return lista

