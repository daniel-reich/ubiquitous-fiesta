
import numpy as np
def climb(stamina, obstacles):
  # https://edabit.com/challenge/Q7oecYfjkq7tHwPoA
  obs_len = len(obstacles)
  n = 1
  while True:
    stam_used = compute_stamina_used(obstacles[n-1], obstacles[n])
    stamina = stamina - stam_used
    if stamina < 0:
      break
    else:
      n = n + 1
    if n >= obs_len:
      break
  return n-1
​
def compute_stamina_used(current, next):
  change = next - current
  if change > 0: # Goes up
    stam_used = np.ceil(change)*2
  else:
    stam_used = np.abs(np.floor(change))
  return stam_used

