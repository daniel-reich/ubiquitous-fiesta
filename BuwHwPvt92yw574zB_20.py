
def list_of_multiples (num, length):
  myList = []
  for x in range(length):
    multiple = (x+1) * num
    myList.append(multiple)
  return myList

