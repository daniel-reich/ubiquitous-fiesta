
import re
def XO(text):
  return len(re.findall(r"[xX]", text)) == len(re.findall(r"[oO]", text))

