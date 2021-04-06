
def count_overlapping(intervals, point):
  return sum([iv[0] <= point and point <= iv[1] for iv in intervals])

