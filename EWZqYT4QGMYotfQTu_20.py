
def tap_code(n):
  if("." not in n): 
    a=[["a","b","ck","d","e"],["f","g","h","i","j"],["l","m","n","o","p"],["q","r","s","t","u"],["v","w","x","y","z"]]  
    ans=''
    for i in n:
      row=0
      col=0
      if(i=="c" or i=="k"):
        row=0
        col=2
      else:
        while(row<5):
          check=0
          col=0
          while(col<5):
            if(a[row][col]==i):
              check=1
              
              break
            col+=1
          if(check==1):
            break
          row+=1
​
      row+=1
      col+=1
      aa="."*row+" "
      bb="."*col+" "
      ans+=(aa+bb)
    return ans[0:len(ans)-1]  
  else:
    a=[["a","b","c","d","e"],["f","g","h","i","j"],["l","m","n","o","p"],["q","r","s","t","u"],["v","w","x","y","z"]]
    n=n.split(" ")
    i=list()
    j=list()
    for x in range(0,len(n),2):
      i.append(len(n[x])-1)
    for x in range(1,len(n),2):
      j.append(len(n[x])-1)
    ans=''
    for x in range(0,len(i)):
      ans+=a[i[x]][j[x]]
    return ans

