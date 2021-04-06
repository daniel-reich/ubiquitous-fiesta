
import re
def make_word_riddle(s):
  A=[x.upper() for x in re.split('in|IN', s)]
  return A[1][0]+A[0]+A[1][1:]

