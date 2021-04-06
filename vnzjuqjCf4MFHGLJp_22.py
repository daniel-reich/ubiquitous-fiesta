
def shift_letters(txt,num):
 space= [n for n,i in enumerate(txt) if i==" "]
 newstring= [i for n,i in enumerate(txt)]
​
 while num!=0:
  if newstring[-1]==" ":
      num=num+1
  newstring.insert(0,newstring[-1])
  newstring.pop(-1)
  num=num-1
 newstring= [i for i in newstring if i!=" "]
​
 for n in space:
      newstring[n:n]=" "
 return "".join(newstring)

