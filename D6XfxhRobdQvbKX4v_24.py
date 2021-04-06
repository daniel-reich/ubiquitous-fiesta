
def first_before_second(s, first, second):
  if ''.join(s).rindex(first)<s.find(second) and s.find(second)!=-1:
    return True
  return False

