
def replace_vowel(word):
  v = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
  return "".join([i if i not in v else v[i] for i in word])

