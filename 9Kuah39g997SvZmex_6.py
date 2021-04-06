
def common_last_vowel(txt):
  vowels = "aeiouAEIOU"
  
  for i in range(len(txt)-1,0,-1):
    if txt[i] in vowels:
      return txt[i].lower()

