
import numpy as np
def straight_digital(number):
  sequence = list(map(int, str(abs(number))))
  difference = np.diff(sequence)
  if number < 100 or not all([True if i == difference[0] else False for i in difference]):
    return "Not Straight"
  elif all(i == sequence[0] for i in sequence):
    return "Trivial Straight"
  elif all(i == difference[0] for i in difference):
    return difference[0]

