
from re import sub
def syllabification(w):
  return sub("(?<!^)([^aAeiou][aAeiou])", ".\\1", w)

