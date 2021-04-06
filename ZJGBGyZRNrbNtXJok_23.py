
def nearest_vowel(s):
  s = ord(s) - 97
  if s < 3:
    return "a"
  elif s < 7:
    return "e"
  elif s < 12:
    return "i"
  elif s < 18:
    return "o"
  else:
    return "u"

