
import re
def no_yelling(phrase):
  phrase = re.sub(r'!+$', r'!',phrase)
  return re.sub(r'\?+$', r'?',phrase)

