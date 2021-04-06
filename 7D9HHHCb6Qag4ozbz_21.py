
def find_zip(txt):
  f=txt.find("zip")
  new_txt=txt[:f]+"xxx"+txt[f+3:]
  return new_txt.find("zip")

