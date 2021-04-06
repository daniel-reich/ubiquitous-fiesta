
def eval_factorial(li1):
     li2=  [i.replace('!','') for i in li1 ]
     newlist=[]
     for j in li2:
         if int(j)>1:
          for i in range(1,int(j)):
             j= int(j)*i
          newlist.append(j)
​
         else:
             newlist.append(1)
​
​
     return(sum(newlist))

