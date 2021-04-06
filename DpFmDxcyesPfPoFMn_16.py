
def isbnx(x):
  if x=="X":
    return 10
  return(int(x))
​
def isbn13(txt):
  print(txt,len(txt))
  c=False
  if len(txt)==10:
    if sum([ isbnx(x)*r for x,r in zip(txt,range(10,0,-1) )])  %11!=0:
      return("Invalid")
    txt="978"+txt 
    c=sum([ isbnx(x)* (2*(r %2)+1) for x,r in zip(txt,range(0,14) )]) %10
    txt=txt[:-1] + str( (isbnx(txt[-1])-c)%10 )
    return(txt)
    
  if len(txt)==13:
    if sum([ int(x)* (2*(r %2)+1) for x,r in zip(txt,range(0,14) )]) %10==0:
      return("Valid")
​
  return("Invalid")

