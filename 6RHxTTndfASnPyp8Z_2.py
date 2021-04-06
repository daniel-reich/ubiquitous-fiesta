
from itertools import takewhile
def compress(chars):
  if len(chars) == 1:
    return chars[0]
  if len(set(chars)) == 1:
    return chars[0] + str(len(chars))
  current = chars[0]
  number = len(list(takewhile(lambda x: x == current,chars)))
  chars = chars[number::]
  string = current
  if number > 1:
    string += str(number)
  return string + compress(chars)

