
def sum_of_vowels(sentence):
  dic = {'a':4, 'e':3, 'i':1}
  return sum(dic[v] for v in sentence.lower() if v in dic)

