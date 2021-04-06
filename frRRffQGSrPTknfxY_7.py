
def digit_count(n):
  arr = []
  for c in str(n):
    arr.append(str(str(n).count(c)))
  return int("".join(arr))

