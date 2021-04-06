
def sum_missing_numbers(lst):
  lst.sort()
  sumList = 0
  for el in lst:
    sumList += el
  expectedSumHigh = lst[len(lst)-1]*(lst[len(lst)-1] + 1)/2
  expectedSumLow = 0
  if lst[0] != 1:
    expectedSumLow = (lst[0] - 1)*(lst[0])/2
  return expectedSumHigh - expectedSumLow - sumList

