
def validate_spelling(txt):
  lstTxt = txt.split(". ")
  return "".join(lstTxt[:-1]) == lstTxt[-1][:-1].upper()

