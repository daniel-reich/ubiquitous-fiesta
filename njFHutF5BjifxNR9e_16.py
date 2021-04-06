
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
def change(x, times):
  temp = x[:]
  for i in range(len(x)):
    j = 1
    while j <= times:
      if i >= j and i < len(x)-j:
        temp[i] -= 1
      j += 1
  return temp
​
x = [3, 3, 3, 3, 3, 3, 3]

