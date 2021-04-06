
properFreq = [329.63,246.94,196.00,146.83,110.00,82.41]
​
def tune(lst):
  pointer = 0
  finalarray = []
  while pointer <6:
    theResult=""
    if lst[pointer] == 0:
      theResult = " - "
    else:
      answer = lst[pointer]/properFreq[pointer]
      theResult=""
      if answer >1.03:
        theResult = "+<<"
      elif answer >1.005:
        theResult = "+<"
      elif answer > 0.995:
        theResult = "OK"
      elif answer > 0.98:
        theResult = ">+"
      elif answer <= 0.98:
        theResult = ">>+"
    finalarray.append(theResult)
    pointer+=1
  return finalarray

