
def seating_students(lst):
  k, occupied = lst[0], set(lst[1:])
  total = 0
  for i in range(1, k):
    if i not in occupied:
      if i % 2 and i + 1 not in occupied:
        total += 1
      if i + 2 <= k and i + 2 not in occupied:
        total += 1
  return total

