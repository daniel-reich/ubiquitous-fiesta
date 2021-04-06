
def count_overlapping(intervals, point):
  return len([[start, end] for start,end in intervals if point in range(start, end+1)])

