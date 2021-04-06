
def sum_of_vowels(sentence):
   return sum({'a': 4, 'e': 3, 'i': 1}.get(x.lower(), 0) for x in sentence)

