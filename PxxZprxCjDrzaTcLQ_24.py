
def vowel_links(txt):
  vowels = "aeiou"
  txt = txt.split()
  
  for i in range(len(txt) - 1):
    if txt[i][-1] in vowels and txt[i + 1][0] in vowels:
      return True
  return False

