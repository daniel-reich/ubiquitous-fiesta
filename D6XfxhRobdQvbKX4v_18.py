
def first_before_second(s, first, second):
  return s.rfind(second)>s.rfind(first) and s.find(second)>s.rfind(first)

