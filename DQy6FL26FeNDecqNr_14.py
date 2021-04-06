
import itertools
​
def correct_stream(user, correct):
  return [1 if i == j else -1 for i, j in zip(user, correct)]

