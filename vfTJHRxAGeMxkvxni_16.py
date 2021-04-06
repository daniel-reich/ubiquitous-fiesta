
def count_overlapping(intervals, point):
  overlaps = 0
  for ints in intervals:
    if point >= ints[0] and point <= ints[-1]:
      overlaps += 1
  return overlaps

