
from statistics import mean
​
def trimmed_averages(lst):
  return round(mean(sorted(lst)[1:-1]))

