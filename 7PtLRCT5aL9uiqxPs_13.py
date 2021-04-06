
def last_dig(a, b, c):
  lastDigitOfA = str(a)[-1]
  lastDigitOfB = str(b)[-1]
  lastDigitOfC = str(c)[-1]
  multiplicationOfAandB = int(lastDigitOfA) * int(lastDigitOfB)
  lastDigitOfMulResult = str(multiplicationOfAandB)[-1]
  return lastDigitOfMulResult == lastDigitOfC

