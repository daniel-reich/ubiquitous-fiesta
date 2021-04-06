
from itertools import repeat
​
def censor(s):
  result = ""
  for word in s.split():
    if len(word) > 4:
      result += ''.join(repeat("*", len(word))) + " "
    else:
      result += word + " "
  return result.strip()

