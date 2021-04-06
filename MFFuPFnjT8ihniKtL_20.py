
import math
def bug_jump(height, time):
  time /= 1000
  duration = 2 * math.sqrt(height)
  if 0 < time < duration:
    pos = height - (time - duration / 2) ** 2
    return [round(pos, 2), 'up' if time < duration / 2 else 'down']
  else:
    return [0, None]

