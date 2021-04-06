
import string
​
def replace(txt, r):
  low, hi = r.split("-")
  letters = string.ascii_lowercase
  low_i = letters.index(low)
  hi_i = letters.index(hi)
  to_replace = letters[low_i:hi_i+1]
  result = ""
  for letter in txt:
    result += letter if letter not in to_replace else "#"
  return result

