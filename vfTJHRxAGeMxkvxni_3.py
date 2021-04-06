
def count_overlapping(intervals, point):
  count=0
  for x in intervals:
    if point>= x[0] and point<=x[1]:
      count+=1
  return count

