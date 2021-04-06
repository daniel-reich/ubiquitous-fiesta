
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
x = [3, 3, 3, 3, 3, 3, 3]
def change(x, times):
  x1 = list(x)
  for i in range(len(x1)):
    j = 1
    while j<=times:
      if i>=j and i < len(x1)-j:
        x1[i] -= 1
      j += 1
  return x1

