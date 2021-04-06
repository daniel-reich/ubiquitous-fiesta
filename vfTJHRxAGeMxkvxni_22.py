
def count_overlapping(intervals, point):
  return sum(1 for a,b in intervals if a <= point <= b)

