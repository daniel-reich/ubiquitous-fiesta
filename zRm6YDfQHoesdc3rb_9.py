
def rectangles(step):
  if step == 1:
    return 1
  else:
    counter = 0
    for i in range(1,step+1):
      counter += i**3
​
    return counter

