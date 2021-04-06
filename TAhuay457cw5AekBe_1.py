
def monkey_talk(txt):
  return " ".join("eek" if w[0] in "aeiou" else "ook" for w in txt.lower().split()).capitalize() + "."

