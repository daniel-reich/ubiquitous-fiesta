
def fibonacci_sequence():
  i = 1
  prev = 0
  l = [0, 1]
  while i < 255:
    new = i + prev
    prev = i
    i = new
​
    if i > 255:
      break
​
    l.append(i)
  return l

