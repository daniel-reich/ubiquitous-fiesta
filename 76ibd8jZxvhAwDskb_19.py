
def tallest_skyscraper(lst):
  col1 = [item[0] for item in lst]
  col2 = [item[1] for item in lst]
  col3 = [item[2] for item in lst]
  col4 = [item[3] for item in lst]
​
  def sortThroughCol(colList):
      total = 0
      for each in colList:
          if(each == 1):
              total = total + 1
      return total
​
  total1 = sortThroughCol(col1)
  total2 = sortThroughCol(col2)
  total3 = sortThroughCol(col3)
  total4 = sortThroughCol(col4)
​
  if(total1 > total2):
      totalRound1 = total1
  else:
      totalRound1 = total2
  
  if(total3 > total4):
      totalRound2 = total3
  else:
      totalRound2 = total4
  if(totalRound1 > totalRound2):
      print(str(totalRound1))
      return totalRound1
  else: 
      print(str(totalRound2))
      return totalRound2

