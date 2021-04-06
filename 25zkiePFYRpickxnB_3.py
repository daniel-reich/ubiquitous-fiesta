
def count_boomerangs(lst):
  boomerNum = 0
  if len(lst) < 2:
    return 0
  for i in range(len(lst) - 2):
    tempList = [lst[i], lst[i+1], lst[i+2]]
    #print(tempList)
    if tempList[0] == tempList[2] and tempList[0] != tempList[1]:
        #print(tempList[0] == tempList[2])
        boomerNum = boomerNum + 1
  return boomerNum

