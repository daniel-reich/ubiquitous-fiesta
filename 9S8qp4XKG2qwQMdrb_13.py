
def ways_to_climb(n):
  count = 0
  if n == 0:
    count += 1
  if n == 1:
    count += 1
  if n > 1:
    count += ways_to_climb(n-1) + ways_to_climb(n-2)
  return count

