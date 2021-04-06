
def fibonacci_sequence():
  fibSeq = [0, 1]
  pointerVal = 0
  while True:
    curNum = fibSeq[pointerVal] + fibSeq[pointerVal + 1]
    if curNum >= 255:
      break
    fibSeq.append(curNum)
    pointerVal += 1
  return fibSeq

