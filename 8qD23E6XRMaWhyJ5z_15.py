
def happiness_number(s):
  num = 0
  num += s.count(':)')
  num += s.count('(:')
  num -= s.count(':(')
  num -= s.count('):')
  return num

