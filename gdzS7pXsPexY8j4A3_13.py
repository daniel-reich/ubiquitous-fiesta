
def count_digits(lst, t):
  newAry = []
  for i in lst:
    temp = ''
    sumVal = 0
    for j in range(0,len(str(i))):
      temp += (str(i)[j])
      if int(str(i)[j]) % 2 is not 0 and t is "odd":
        sumVal += 1
      elif int(str(i)[j]) % 2 is 0 and t is "even":
        sumVal += 1
      else:
        pass
    newAry.append(sumVal)
  return(newAry)

