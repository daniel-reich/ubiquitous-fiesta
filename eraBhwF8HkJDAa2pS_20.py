
def pirates_killed(gold, tolerance):
  max_val = max(gold)
  kills = [el for (i,el) in enumerate(tolerance) if tolerance[i] < max_val - gold[i]]
  return len(kills) > 0

