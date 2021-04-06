
from math import pi
from itertools import accumulate
​
# a list of the length of each required word
pi_digits = list(map(int, str(pi).replace('.', '')[:15]))
# the start index of each word in txt argument
txt_index = [0] + list(accumulate(pi_digits))
​
def pilish_string(txt):
  if not txt: return txt
  # this list comprehension iterates through the pi_digits array and extracts each word of the given length
  # the start index is looked up in the accumulated start position of each word in the txt_index array
  words = [txt[txt_index[ix]:txt_index[ix]+l] for ix, l in enumerate(pi_digits) if txt_index[ix] < len(txt)]
  # if the last word is shorter than the given pi digit length pad it to the proper length
  pad = pi_digits[len(words)-1] - len(words[-1])
  if pad > 0:
    words[-1] += words[-1][-1] * pad
  return ' '.join(words)

