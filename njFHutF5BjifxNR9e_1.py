
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
def change(x, times):
  l = x.copy()
  for i in range(len(l)):
    j = 1
    while j <= times:
      if i >= j and i < len(l)-j:
        l[i] -= 1
      j += 1
  return l
​
x = [3, 3, 3, 3, 3, 3, 3]

