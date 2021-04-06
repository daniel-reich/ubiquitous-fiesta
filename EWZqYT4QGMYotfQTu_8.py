
def tap_code(text):
  l=[
  ["a","b","c\k","d","e"],
  ["f","g","h","i","j"],
  ["l","m","n","o","p"],
  ["q","r","s","t","u"],
  ["v","w","x","y","z"],
  ]
​
  final=[]
  temp=[]
  if text.isalpha():
    for k in text:
      for i in range(len(l)): 
        for j in range(len(l[i])):
          if l[i][j] is k:
            s="."*(i+1)+" "*1+"."*(j+1)
            temp.append(s)
      if k is "c" or k is "k":
        temp.append(". ...")
                
    final.append(" ".join(temp))
    temp.clear()
    return final[0]
  else:
    r=text.split()
    row=[r[i].count(".")-1 for i in range(0,len(r),2)]
    col=[r[i].count(".")-1 for i in range(1,len(r),2)]
    for r,c in zip(row,col) :
      if l[r][c] is "c\k":
        temp.append("c")
      else:
        temp.append(l[r][c])
    final.append("".join(temp))
    return final[0]

