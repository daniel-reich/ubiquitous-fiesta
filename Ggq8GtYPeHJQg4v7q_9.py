
def replace_vowels(txt, ch):
  l=['a','e','i','o','u']
  x=txt
  for i in txt:
    if i in l:
      x=x.replace(i,ch)
  return x

