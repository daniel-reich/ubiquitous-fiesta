
import re
def blah_blah(txt, n):
  return re.sub('\w+', 'halb', txt[::-1], count=n)[::-1]+'...'

