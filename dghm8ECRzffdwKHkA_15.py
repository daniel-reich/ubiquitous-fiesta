
import string
def capital_letters(txt):
  count = 0
  for i in txt:
    if i in string.ascii_uppercase:
      count += 1
  return count

