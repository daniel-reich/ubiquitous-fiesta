
def digit_sort(lst):
  x = sorted(lst, key=lambda x: len(str(x)), reverse = True)
  while True:
    c = 0
    for i in range(len(x)-1):
      if len(str(x[i])) == len(str(x[i+1])):
        if x[i] > x[i+1]:
          x[i],x[i+1] = x[i+1], x[i]
          c += 1
    if c == 0:
      break
  return x

