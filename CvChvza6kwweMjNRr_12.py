
def split_code(item):
  newlst = []
  check = 0
  for x in item:
    if x in "1234567890":
      newlst.append(item[0:check])
      intifier = item[check:len(item)]
      newlst.append(int(intifier))
      return newlst
    else:
      check+=1
      print(check)

