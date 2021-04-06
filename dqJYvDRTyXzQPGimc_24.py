
def is_unfair_hurdle(hurdles):
  check_distance = len(hurdles[0].split('#')[1])
  check_height = len(hurdles)
  return not(check_distance > 3 and check_height < 4)

