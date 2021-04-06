
import re
def hangman(phrase, lst):
  pat = re.compile(r'[^'+''.join(lst)+'\W\d]',re.I)
  return pat.sub('-',phrase)

