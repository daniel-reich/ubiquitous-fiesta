
def score_it(s):
  nest = 0
  d = ""
  total = 0
  for c in s:
    if c.isdigit():
      d += c
    elif((c == '(' or c == ')') and d):
      total += (int(d) * nest)
      d = ""
    if c == '(': nest += 1
    elif c == ')': nest -= 1
  return total

