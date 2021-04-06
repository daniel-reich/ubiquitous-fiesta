
def count_overlapping(intervals, point):
  return ([i[0] <= point <= i[1] for i in intervals]).count(True)

