
def replace_vowels(txt, ch):
  new_txt=""
  search=['a','e','i','o','u']
  for i in range(len(txt)):
    if txt[i] in search:
      new_txt+=ch
    else:
      new_txt+=txt[i]
  return new_txt

