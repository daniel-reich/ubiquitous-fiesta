
def validate_spelling(txt):
  return "".join(txt.split(". ")[:-1]).lower() == txt.split(". ")[-1][:-1].lower()

