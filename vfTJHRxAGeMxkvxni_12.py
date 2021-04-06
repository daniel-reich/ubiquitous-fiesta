
def count_overlapping(intervals, point):
  return sum(point in range(a, b+1) for a, b in intervals)

