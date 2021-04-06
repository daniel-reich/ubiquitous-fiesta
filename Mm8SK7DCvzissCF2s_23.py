
import string
def in_alpha(word):
  nums = list(enumerate(string.ascii_lowercase, 1))
  letters = [i.lower() for i in word if i.isalpha()]
  summ = 0
  for i in letters:
    for a, b in nums:
      if b == i:
        summ += a
  return not summ % 2

