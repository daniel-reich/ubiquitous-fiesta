
def sum_of_vowels(sentence):
  s = {"A":4, "E":3, "I":1}
  l = [i.upper() for i in sentence if i in 'aeiouAEIOU']
  return sum(s[i] for i in l if i in s)

