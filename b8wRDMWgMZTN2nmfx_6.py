
def equal(a, b, c):
  count = 0
  if a == b or b==c or a==c:
    count += 2
  if a == b == c:
    count += 1
  return count

