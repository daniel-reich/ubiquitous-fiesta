
def block_player(a, b):
  if abs(b - a) % 3 == 0:
    step = 3
    colNum = b % 3
    possibilityList = range(colNum, (colNum+2*3)+1, step)
  elif b % 2 == 0 and a % 2 == 0:
    list1 = [0, 4, 8]
    list2 = [2, 4, 6]
    if a in list1 and b in list1:
      possibilityList = list1
    else:
      possibilityList = list2
  else:
    step = 1
    rowNum = b // 3
    possibilityList = range(rowNum*3, rowNum*3+3, step)
​
  return list(set(possibilityList) - set([a, b]))[0]

