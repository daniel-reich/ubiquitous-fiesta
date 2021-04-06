
def divisible_by_b(a, b):
  i = a + 1
  while i % b != 0:
    if i % b == 0:
      break
    i += 1
  return i

