
import re
def validate_spelling(txt):
  w, target = txt.rsplit(' ',1)
  return re.sub(r'[\.\s]','',w).lower() == target[:-1].lower()

