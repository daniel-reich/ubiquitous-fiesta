
import re
def is_alpha(word):
  word = ''.join(re.findall(r'[a-z]*', word.lower()))
  return sum([ord(i)-96 for i in word]) % 2 == 0

