
def count_overlapping(intervals, point):
  return len([i for i in intervals if point >=i[0] and point<=i[1]])

