
import re
def super_reduced_string(txt):
  txt1 = ""
  while txt != txt1:
    txt1 = txt
    txt = re.sub(r"([a-z])\1", "", txt)
  if txt == "":
    return "Empty String"
  else:
    return txt

