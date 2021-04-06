
def count_overlapping(intervals, point):
  return sum([1 if point in list(range(intervals[i][0], intervals[i][1] + 1)) else 0 for i in range(len(intervals))])

