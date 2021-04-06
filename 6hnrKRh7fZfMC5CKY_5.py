
def look_and_say(n):
  lister = list(str(n))
  newlst = []
  string = ""
  stringer = ""
  if len(list(str(n)))%2 == 1:
    return "invalid"
  else:
    for i in lister:
      j = int(i)
      newlst.append(j)
    for i in range(len(newlst)):
      if i%2 == 0:
        stringer = newlst[i]*str(newlst[i+1])
        string+= stringer
  return int(string)

