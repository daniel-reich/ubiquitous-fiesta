
def maxmin(no):
   lst=[i for i in str(no)]
   lst1=lst.copy()
   finallst=[no]
   for k in range(len(lst)):
    for n in range(1,len(lst)):
     lst1[k], lst1[n] = lst1[n], lst1[k]
     if len(str(int("".join(lst1)))) == len(lst):
       finallst.append(int("".join(lst1)))
     lst1 = lst.copy()
​
​
   return(max(finallst),min(finallst))

