
import re
def syllabification(word):
  return re.sub(r'([^Aaeoui])([Aaeoui])', r'.\1\2', word).strip(".")

