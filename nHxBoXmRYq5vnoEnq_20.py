
def vowels(string):
  if string=="":
    return 0
  vowel = 0
  if string[0] in ["e","a","i","o","u"]:
    vowel = 1
  return vowel+vowels(string[1:])

