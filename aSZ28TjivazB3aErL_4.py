
from re import search
def letters_only(s):
  return search(r'[^a-z\s]', s) == None and s != ''

