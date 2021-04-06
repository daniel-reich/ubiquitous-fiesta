
import re
​
def increment_string(txt):
  word, number = re.search("(\D*)(\d*)", txt).groups()
  if not number: return word + "1"
  number_int = (int(number)) + 1
  return word + (len(number)-len(str(number_int)))*"0" + str(number_int)

