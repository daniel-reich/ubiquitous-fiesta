
def monkey_talk(txt):
  return " ".join(["ook" if x[0] not in "aeiouAEIOU" else "eek" for x in txt.split(" ")]).capitalize()+"."

