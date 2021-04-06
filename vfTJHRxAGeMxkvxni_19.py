
def count_overlapping(intervals, point):
  j = 0
  for i in intervals:
    if point in range(i[0], i[1]+1):
      j += 1
  return j

