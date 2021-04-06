
def alpha_range(start, stop, step=1):
  if step == 0 or step <= -26 or step >= 26:
    return "step must be a non-zero value between -26 and 26, exclusive"
  elif start.isupper() != stop.isupper():
    return "both start and stop must share the same case"
  elif stop < start:
    return [chr(r) for r in range(ord(stop), ord(start)+1)][::step]
  else:
    return [chr(r) for r in range(ord(start), ord(stop)+1)][::step]

