
def count_overlapping(intervals, point):
  count = 0
  for i in intervals:
    if i[0] == point or i[1] == point:
      count += 1
    else:
      for y in range(i[0],i[1]):
        if y == point:
          count += 1
  return count

