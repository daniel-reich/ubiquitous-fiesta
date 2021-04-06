
def count_overlapping(intervals, point):
  return sum(a <= point <= b for a, b in intervals)

