
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
def change(x, times):
  y = x.copy()
  for i in range(len(y)):
    j = 1
    while j <= times:
      if i >= j and i < len(y)-j:
        y[i] -= 1
      j += 1
  return y
​
x = [3, 3, 3, 3, 3, 3, 3]

