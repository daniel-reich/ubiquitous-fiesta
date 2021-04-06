
def nearest_vowel(s):
  if "a" <= s <= "c":
    return "a"
  elif "d" <= s <= "g":
    return "e"
  elif "h" <= s <= "l":
    return "i"
  elif "m" <= s <= "r":
    return "o"
  else:
    return "u"

