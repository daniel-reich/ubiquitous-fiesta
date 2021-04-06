
def look_and_say(start, n):
  string=str(start)
  newstring=""
  arr=[start]
  
  while n>1:
    newstring=""
    i=0
    checking=string[0]
    count=0
    while i<len(string):
      if string[i]==checking:
        count+=1
        i+=1
        continue
      else:
        newstring+=str(count)+checking
        checking=string[i]
        count=0
        continue
    newstring+=str(count)+checking
    arr.append(int(newstring))
    string=newstring
    n-=1
  
  return arr

