
import string
​
​
def is_pandigital(n):
  return set(char for char in str(n)) == set(char for char in string.digits)

