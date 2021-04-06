
import string
def validate_spelling(txt):
  t = ''.join(txt.split()[:-1]).translate(str.maketrans('', '', string.punctuation))
  x = txt.split()[-1].translate(str.maketrans('', '', string.punctuation))
  return t.lower() == x.lower()

