
from collections import Counter
​
def route_diff(directions):
  steps = Counter(directions)
  minsteps = abs(steps['N'] - steps['S']) + abs(steps['W'] - steps['E'])
  return len(directions) - minsteps

