
def validate_spelling(txt):
  spell = (("".join(txt.split(" ")[:-1])).replace(".", "")).lower()
  word = txt.split(" ")[-1][:-1]
  return spell == word.lower()

