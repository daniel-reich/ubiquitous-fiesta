
def soroban(frame):
  for line in frame:
    if list(set(line))[0] == '-':
      dividingLine = frame.index(line)
  frame.pop(dividingLine-1)
  frame.pop(dividingLine)
  dividingLine -=1
  upperLine = frame[:dividingLine][0]
  bottomLines = frame[dividingLine+1:]
  total = [0]*len(bottomLines[0])
​
  for lines in bottomLines:
    temp = -1
    for i in lines:
      temp+=1
      if i == '|':
        value = bottomLines.index(lines)+1
        total[temp] += value
​
  temp = -1
  for i in upperLine:
    temp += 1
    if i == '|':
      total[temp] += 5
  a = ''.join(str(x) for x in total)
  return int(a)

