
from itertools import accumulate 
​
def currently_winning(scores):
  y_scores = [y for i, y in enumerate(scores) if i % 2 == 0]
  o_scores = [y for i, y in enumerate(scores) if i % 2 != 0]
  y_tot_scores = list(accumulate(y_scores))
  o_tot_scores = list(accumulate(o_scores))
  scores = list(zip(y_tot_scores, o_tot_scores))
  return ["Y" if x[0] > x[1] else "O" if x[1] > x[0] else "T" for x in scores]

