
import re
def club_entry(word):
  A=re.findall(r'(.)\1', word)
  return (ord(A[-1])-ord('a')+1)*4

