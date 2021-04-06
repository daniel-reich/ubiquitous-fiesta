
def first_before_second(s, first, second):
  index = s.index(second)
  sub = s[index:]
  if first in sub:
    return False;
  return True;

