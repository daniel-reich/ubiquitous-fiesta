
def dashed(txt):
  vowel = "aeiou"
  return "".join(["-{}-".format(i) if i.lower() in vowel else i for i in txt])

