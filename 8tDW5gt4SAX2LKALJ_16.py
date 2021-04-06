
from functools import reduce
def reachable_bombs(m):
   r=[[set() for col in range(len(m[0]))] for row in range(len(m))]
   for i in range(len(m)):
     for j in range(len(m[0])):
       if m[i][j] == '+':
         r[i][j]=set([len(m[0])*i+j]+list((r[i-1][j] if i>0 else []))+list((r[i][j-1] if j>0 else []))+reachables(m,(i,j+1))+reachables(m,(i+1,j)))
       if m[i][j] == 'x':
         r[i][j]=set([len(m[0])*i+j]+list((r[i-1][j-1] if i>0 and j>0 else []))+list((r[i-1][j+1] if i>0 and j<len(m[0])-1 else []))+reachables(m,(i+1,j-1))+reachables(m,(i+1,j+1)))
   rb=[[set() for col in range(len(m[0]))] for row in range(len(m))]
   for i in range(len(m)):
     for j in range(len(m[0])):
       for k in r[i][j]:
           rb[i][j]=rb[i][j]|r[k//len(m[0])][k%len(m[0])]
   return rb
​
def reachables(m,t):
   i,j=t
   if i<0 or i>len(m)-1:
      return []
   if j<0 or j>len(m[0])-1:
      return []
   if m[i][j] == '0':
      return []
   if m[i][j] == '+':
      return [len(m[0])*i+j]+reachables(m,(i,j+1))+reachables(m,(i+1,j))
   if m[i][j] == 'x':
      return [len(m[0])*i+j]+reachables(m,(i+1,j-1))+reachables(m,(i+1,j+1))
​
def min_bombs_needed(m):
   bombs=[]
   for i in range(len(m)):
       for j in range(len(m[0])):
           bombs=bombs+[i*len(m[0])+j] if m[i][j]=='+' or m[i][j]=='x' else bombs
   bs=set(bombs)
   rb=reachable_bombs(m)
   rbs=reduce(lambda x,y: x+y, rb, [])
   rbs=set(map(lambda x: frozenset(x), rbs))
   rbs=sorted(rbs,key=len,reverse=True)
   s=set()
   c=0
   for i in range(len(rbs)):
      if not rbs[i]&s==rbs[i]:
         c+=1
         s=s|rbs[i]
      if s==bs:
        break
   return c

