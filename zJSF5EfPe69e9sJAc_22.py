
def censor_string(txt, lst, char):
  lista = txt.split()
  word = ''
​
  for i in lista:
    if i in lst:
      i = char*len(i)
    word += i + " "
  return word[:-1]

