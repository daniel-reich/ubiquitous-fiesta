
def count_overlapping(intervals, point):
  count = 0
  for iv in intervals:
    if point in range(iv[0], iv[1]+1):
      count+=1
  return count

