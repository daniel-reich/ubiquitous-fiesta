
def can_traverse(lst):
 lst1= [list(i).count(1) for i in zip(*lst)]
 count=0
 for n in range(len(lst1)-1):
    if lst1[n]==lst1[n+1]+1 or lst1[n]==lst1[n+1]-1 or lst1[n]==lst1[n+1]:
       count+=1
 return count==8

