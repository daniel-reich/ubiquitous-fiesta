
def count_overlapping(intervals, point):
  return sum(min(x)<=point<=max(x) for x in intervals)

