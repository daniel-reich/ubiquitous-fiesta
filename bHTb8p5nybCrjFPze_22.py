
def inclusive_list(startNum, endNum):
  my_list = []
  if startNum>endNum:
    my_list = [startNum]
  else:
    while startNum<endNum+1:
      my_list.append(startNum)
      startNum +=1
      
  return my_list

