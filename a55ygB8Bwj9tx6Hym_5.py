
def steps_to_convert(txt):
  lower_count = len([ch for ch in txt if ch.islower()])
  return min(lower_count, len(txt) - lower_count)

