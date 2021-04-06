
def change(x, times):
  xx=[n for n in x]
  for i in range(len(x)):
    j = 1
    while j <= times:
      if i >= j and i < len(x)-j:
        xx[i] -= 1
      j += 1
  return xx
​
x = [3, 3, 3, 3, 3, 3, 3]

