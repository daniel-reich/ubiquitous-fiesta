
def shuffle_count(num):
  originalList = [i for i in range(1,num+1)]
  inputList = [i for i in range(1,num+1)]
  shuffledList = []
  c = 0
  while True:
    c = c+1
    firstHalf = [inputList[i] for i in range(len(inputList)//2) ]
    secondHalf = [inputList[i] for i in range(len(inputList)//2,len(inputList)) ]
    zippedList = list(zip(firstHalf,secondHalf))
    shuffledList = [e for e1 in zippedList for e in e1]
    inputList = shuffledList
    if inputList==originalList:
      break
  return c

