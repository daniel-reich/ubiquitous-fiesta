
# As it stands, only 1/4 tests pass
# Fix the code so that all tests pass
def change(x, times):
  if times > 0:
    return [x[0]] + change([i-1 for i in x[1:-1]], times-1) + [x[-1]]
  return x
​
x = [3, 3, 3, 3, 3, 3, 3]

