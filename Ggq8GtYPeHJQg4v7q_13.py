
vowels = ['a','e','i','o','u']
​
def replace_vowels(txt, ch):
  for i in txt:
    if i in vowels:
      txt = txt.replace(i, ch)
  return txt

