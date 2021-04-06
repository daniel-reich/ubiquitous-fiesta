
def monkey_talk(txt):
  vowels = frozenset("aeiou")
  txt = txt.lower()
  words = txt.split()
  result = []
  for word in words:
    if word[0] in vowels:
      result.append("eek")
    else:
      result.append("ook")
  return (" ".join(result)).capitalize() + "."

