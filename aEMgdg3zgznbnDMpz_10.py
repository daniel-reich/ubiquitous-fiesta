
import re
def rotated_words(txt):
  p=r'(?i)^[hinosxzmw]+$'
  A=set(txt.split())
  c=0
  for x in A:
    if bool(re.match(p,x)):
      c+=1
  return c

