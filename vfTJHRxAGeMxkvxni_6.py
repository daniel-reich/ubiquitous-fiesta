
def count_overlapping(intervals, point):
  count=0
  for i in intervals:
    if point>=i[0] and point<=i[1]: count+=1
  return count

