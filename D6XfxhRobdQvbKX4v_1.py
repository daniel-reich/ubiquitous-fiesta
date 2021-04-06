
def first_before_second(s, first, second):
  return not(first in s[s.index(second):])

