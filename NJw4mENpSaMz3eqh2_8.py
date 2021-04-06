
def is_undulating(number):
  isUndulating = False
  num1 = ""
  num2 = ""
  numberStr = str(number)
  numberLen = len(numberStr)
  oddIndeces = [1]
  evenIndeces = [0]
  numberOfEvenIndeces = 0
  numberOfOddIndeces = 0
  if numberLen % 2 == 1:
      numberOfEvenIndeces = int(numberLen/2) + 1
      numberOfOddIndeces = int(numberLen/2)
  elif numberLen % 2 == 0:
      numberOfOddIndeces = int(numberLen/2)
      numberOfEvenIndeces = int(numberLen/2)
  for i in range(numberOfOddIndeces-1):
      nextOddIndex = oddIndeces[-1] + 2
      oddIndeces.append(nextOddIndex)
  for i in range(numberOfEvenIndeces-1):
      nextEvenIndex = evenIndeces[-1] + 2
      evenIndeces.append(nextEvenIndex)
  if len(numberStr) >= 3:
      num1 = numberStr[0]
      num2 = numberStr[1]
      for i in oddIndeces:
          if numberStr[i] == num2:
              isUndulating = True
          else:
              isUndulating = False
              break
      for i in evenIndeces:
          if isUndulating == False:
              break
          elif numberStr[i] == num1:
              isUndulating = True
          else:
              isUndulating = False
              break
  return isUndulating

