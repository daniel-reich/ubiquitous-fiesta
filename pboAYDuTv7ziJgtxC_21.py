
def min_turns(current, target):
  a = []
  for i in list(zip(current, target)):
    diffs = abs(int(i[0]) - int(i[1]))
    a.append(10 - diffs if diffs > 5 else diffs)
​
  return sum(a)

