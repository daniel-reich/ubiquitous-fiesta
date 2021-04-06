
def replace_vowel(word):
  d = {'a':'1','e':'2','i':'3','o':'4','u':'5'}
  for key, value in d.items():
    word = word.replace(key,value)
  return word

