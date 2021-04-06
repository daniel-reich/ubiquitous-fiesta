
value = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1,
'J':8, 'K':5, 'L':2, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1,
'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10 }
def best_words(lst):
  points = {}
  for w in lst:
    points[w]= code(w) 
  max_value = max(points.values())
  max_keys = [k for k, v in points.items() if v == max_value]
  return list(filter(lambda x: x in max_keys, lst))
​
def code(s):
  sum = 0 
  for c in s:
    sum += value[c.upper()]
  return sum

