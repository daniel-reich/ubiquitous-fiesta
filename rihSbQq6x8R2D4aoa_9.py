
def alpha_range(start, stop, step=1):
  if step == 0 or step < -26 or step > 26:
    return "step must be a non-zero value between -26 and 26, exclusive"
  if start.islower() and stop.isupper() or start.isupper() and stop.islower():
    return "both start and stop must share the same case"
  if step>0:
    start, stop = min(ord(start), ord(stop)), max(ord(start), ord(stop))
    return [chr(i) for i in range(start, stop+1, step)]
  else:
    start, stop = max(ord(start), ord(stop)), min(ord(start), ord(stop))
    return [chr(i) for i in range(start, stop-1, step)]

