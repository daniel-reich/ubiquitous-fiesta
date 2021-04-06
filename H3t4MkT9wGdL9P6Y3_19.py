
def oddish_or_evenish(num):
  strNum = str(num)
  newNum = 0
  for i in strNum:
    newNum += int(i)
  if(newNum % 2 > 0):
    return "Oddish"
  else:
    return "Evenish"

