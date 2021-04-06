
def sum_of_vowels(sentence):
  a = sentence.lower().count('a')*4
  e = sentence.lower().count('e')*3
  i = sentence.lower().count('i')
  return a+e+i

