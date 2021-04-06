
def count_overlapping(intervals, point):
  return sum(1 for x in intervals if point in range(x[0],x[1]+1))

