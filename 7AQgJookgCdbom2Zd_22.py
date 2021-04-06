
import re
def f(w):
  if(re.match(r'^[aeiouAEIOU]',w)):
    return re.sub(r'(\W*)(\w+)(\W*)',r'\1\2way\3',w)
  return re.sub(r'(\W*)(\w)(\w+)(\W*)',r'\1\3\2ay\4',w)
def pig_latin(txt):
  l = txt.split()
  return (" ".join(map(f,l))).capitalize()
print(pig_latin("Cats are great pets."))

