
def last_ancestor(folders,X,Y):
    a,b,n,p =[],[],0,0
​
    while n<=len(folders):
     for i,j in folders.items():
       if X in j or X==i:
         a.append(X)
         a.append(i)
         X=i
     n+=1
​
    while p<=len(folders):
     for i,j in folders.items():
       if Y in j or Y==i:
         b.append(Y)
         b.append(i)
         Y=i
     p+=1
​
    for i in a:
      if i in b:
        return (i);break

