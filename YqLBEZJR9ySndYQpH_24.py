
def staircase(n):
  stairList = []
  if n < 0:
    usNum, hashNum, stairs = 0, (n * -1), (n * -1)
  else:
    usNum, hashNum, stairs = (n - 1), 1, n
​
  for i in range(stairs):
    for i in range(usNum):
      stairList.append("_")
    for i in range(hashNum):
      stairList.append("#")
    stairList.append("\n")
    if n < 0:
      usNum += 1
      hashNum -= 1
    else:
      usNum -= 1
      hashNum += 1
​
  stairList.pop()
  stairStr = "".join(stairList)
  return(stairStr)

