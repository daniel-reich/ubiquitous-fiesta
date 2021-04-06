
def count_overlapping(intervals, point):
  n = 0
  for interval in intervals:
    if point in range(interval[0],interval[1]+1):
      n += 1
  return n

