
import re
​
def validate_spelling(txt):
  txt = txt.split(" ")
  t1 = re.sub('[^A-Za-z0-9]+', '', txt[-1]).lower()
  t2 = re.sub('[^A-Za-z0-9]+', '', str(txt[0:-1])).lower()
  return t1 == t2

