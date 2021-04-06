
import re
def super_reduced_string(txt):
  while True:
    nex = re.sub(r'(.)\1','',txt)
    if nex == txt:
      break
    txt = nex
  return txt if txt else "Empty String"

