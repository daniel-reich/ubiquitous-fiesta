
def first_before_second(s, first, second):
  if s.rindex(first) < s.index(second):
    return True
  else:
    return False

