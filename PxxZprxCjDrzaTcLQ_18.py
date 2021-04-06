
def vowel_links(txt):
  vowels = list("aeiou")
  txt = txt.split(" ")
  for i in range(len(txt)):
    try:
      if txt[i][-1] in vowels and txt[i+1][0] in vowels:  
        return True;
    except:
      pass;
  return False;

