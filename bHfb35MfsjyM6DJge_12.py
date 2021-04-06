
from collections import Counter
​
def route_diff(directions):
  c = Counter(directions)
  return len(directions) - (abs(c['N'] - c['S']) + abs(c['E'] - c['W']))

