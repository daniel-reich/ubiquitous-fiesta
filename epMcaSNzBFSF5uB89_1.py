
from itertools import accumulate as acc
​
def currently_winning(scores):
  return ["YOT"[(y < o) + (y == o) * 2] for y, o in zip(acc(scores[::2]), acc(scores[1::2]))]

