
def count_overlapping(intervals, point):
  count = 0;
  for x in intervals:
    if x[0] <= point and point <= x[1]:
      count += 1
  return count

