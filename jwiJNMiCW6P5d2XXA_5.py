
import re
def does_rhyme(str_1, str_2):               # Rhyme Time
  str_1, str_2 = str_1.lower().split()[-1], str_2.lower().split()[-1]
  return re.findall(r'[aeiou]', str_1) == re.findall(r'[aeiou]', str_2)

