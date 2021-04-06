
def count_overlapping(intervals, point):
  m=0
  for n in intervals:
    if n[0]<=point<=n[1]:
        m+=1
  return m

