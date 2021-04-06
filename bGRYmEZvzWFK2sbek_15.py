
from string import ascii_lowercase
from re import sub
​
def get_missing_letters(s):
  return sub('[{} ]'.format(s), '', ascii_lowercase)

