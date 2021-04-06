
def count_overlapping(intervals, point):
  count = 0
  for interval in intervals:
    if (interval[0] <= point) and (point <= interval [1]):
      count += 1
  return count

