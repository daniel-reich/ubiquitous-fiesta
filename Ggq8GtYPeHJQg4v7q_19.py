
def replace_vowels(txt, ch):
  for i in txt:
        if i in "aeiouAEIOU":
           txt=txt.replace(i,ch) 
  return txt

