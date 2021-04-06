
import re
def syllabification(word):
  return re.sub("(?<!^)(?=.[aAeiou].{0,2})",".",word)

