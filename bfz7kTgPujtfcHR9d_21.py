
def x_pronounce(sentence):
  b=sentence.split(" ")
  a=len(b)
  newStr=""
  f=""
  for i in range(0,a):
    c=b[i]
    d=len(c)
    if(c=="x" and d==1):
      f="ecks"
    elif(c[0]=="x"):
      e="z"
      f=e+c[1:]
    elif(c.count("x")>0):
      for j in range(0,d):
        if(c[j]=="x"):
          f=c[0:j]+"cks"+c[j+1:]
    else:
      f=c
    if(i==0):
      newStr=newStr+f
    else:
      newStr=newStr+" "+f
  return newStr

