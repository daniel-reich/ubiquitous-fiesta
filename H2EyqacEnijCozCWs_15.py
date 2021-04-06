
def first_n_vowels(txt, n):
  mystr = ''
  vowels = ['a','e','i','o','u']
  for i in range (len(txt)):
    if txt[i] in vowels and n>0:
      mystr += txt[i]
      n -= 1
  if (n>0):
    return "invalid"
  return mystr

