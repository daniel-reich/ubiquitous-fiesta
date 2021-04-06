
import functools
​
def bugger(num):
  lst = [int(i) for i in str(num)]
  count = 0
  while len(lst) != 1:
    num = functools.reduce((lambda x, y: x * y), lst)
    count += 1
    lst = [int(i) for i in str(num)]
  return count

