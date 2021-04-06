
def find_a_seat(n, lst):
  max_capacity = n // len(lst)
  for i in range(len(lst)):
    x = int((lst[i] / max_capacity) * 100)
    if x <= 50.0:
      return i
  return -1

