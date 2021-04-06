
def time_sum(times):
  # return list of [0, 0, 0] if input is empty
  if not times:
    return [0, 0, 0]
  # convert string into an array of integers
  to_int = [map(int, time.split(":")) for time in times]
  # zip array into a list of tuples, sum the tuples
  [hours, minutes, seconds] = [sum(t) for t in zip(*to_int)]
  # normalize times with divmod (creates tuples), destructuring
  [h, [more_than_60_m, m], [more_than_60_s, s]] = [hours , divmod(minutes, 60), divmod(seconds, 60)]
  # sum/arrange tuples 
  return [h + more_than_60_m, m + more_than_60_s , s]

