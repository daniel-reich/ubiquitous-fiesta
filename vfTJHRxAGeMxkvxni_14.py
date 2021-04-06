
def count_overlapping(intervals, point):
  c = 0
  for i in intervals:
    if point >= i[0] and point <= i[1]:
      c += 1
  return c

