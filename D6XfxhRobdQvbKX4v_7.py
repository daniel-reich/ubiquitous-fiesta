
def first_before_second(s, first, second):
# if first not in s or second not in s return True
  return s.rfind(first) < s.find(second)

