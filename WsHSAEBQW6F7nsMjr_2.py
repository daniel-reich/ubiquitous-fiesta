
from statistics import mean
​
def flatten_the_curve(lst):
    return [round(mean(lst), 1) for n in lst]

