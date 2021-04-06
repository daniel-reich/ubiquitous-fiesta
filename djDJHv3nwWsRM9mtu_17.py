
import re
def validate_spelling(txt):
  return ''.join(i for i in re.split('\.\s', txt.lower())[:-1]) in txt.lower()

