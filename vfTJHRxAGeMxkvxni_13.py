
def count_overlapping(intervals, point):
  return sum([1 for n in intervals if (n[0] <=point and n[1]>=point) ])

