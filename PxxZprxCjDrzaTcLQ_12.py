
def vowel_links(txt):
  txt=txt.split()
  vowel = 'aeiou'
  for i in range(len(txt)-1):
    if txt[i][-1] in vowel and txt[i+1][0] in vowel:return True
  return False

