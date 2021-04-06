
import re
def syllabification(word):
  pattern = r'[\w\?][aAeiou][^aAeiou]{0,2}(?![aAeiou])'
  out = re.findall(pattern, word)
  return '.'.join(out)

