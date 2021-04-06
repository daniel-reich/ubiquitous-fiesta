
def separate_numbers(s):
  for size in range (1, int(len(s) / 2)): #goes through all possible sizes of first numbers
    firstNum = ""
    size9 = size + 1  #if all '9's, length of next string + 1
    for i in range (size):
      firstNum += s[i]  #adds all i to currentNum
      if (s[i] != "9"):   #if not all '9's, length of next string is the same
        size9 = size
    remainingDigits = len(s) - size
    print("firstNum:", firstNum)
    latestNum = int(firstNum)
    x = True
    #len(str(latestNum))
    currentIndex = size
    print("Initial currentIndex:", currentIndex)
    while(remainingDigits > 0):
      print("In while loop")
      print("remainingDigits:", remainingDigits)
      currentNum = ""
      print("for i in range(" + str(currentIndex) + ", " + str(currentIndex + size9))
      for i in range(currentIndex, currentIndex + size9): 
        print("i:", i)
        currentNum += str(s[i])
      print("int(currentNum) - latestNum: " + currentNum + " - " + str(latestNum))
      if (int(currentNum) - latestNum != 1):
        print("Breaks while loop")
        x = False
        break
      latestNum = int(currentNum)
      size9 += 1
      for i in str(latestNum):
        if (i != "9"):
          size9 -= 1
          break
      remainingDigits -= len(str(latestNum))
      currentIndex += len(str(latestNum))
      print("currentIndex:", currentIndex)
    if x: 
      return "YES " + str(firstNum)
    print("first for loop done")
  return "NO"

