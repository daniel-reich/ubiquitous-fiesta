
def count_overlapping(intervals, point):
  a = []
  for x in intervals:
    if point in range(x[0],x[1]+1):
      a.append(x)
  return len(a)

