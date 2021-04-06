
def common_last_vowel(txt):
  txt=txt.lower()
  lst=txt.split()
  vowel='aeiou'
  for i in lst[-1][::-1]:
    if i in vowel:
      return i

