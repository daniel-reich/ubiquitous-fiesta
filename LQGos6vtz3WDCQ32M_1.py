
def Kaprekar(n):
  st='\n---------- The Mysterious Number 6174 ----------\n\n'
  err='Error, n cannot be a repdigit.'
  end='\n\n------------------------------------------------'
  lst=kap(n)
  if not lst: return st+err+end
  ni='Number of iterations: '+str(len(lst))+'\n\nIterations:\n\n'
  it='\n'.join('Iteration Nr. {}: {} - {} = {}'.format(i,b,a,m) for i,b,a,m in lst)
  return st+ni+it+end
​
def kap(n):
  lst,i,m=[],0,(4-len(str(n)))*'0'+str(n)
  if len(set(m))==1: return 0
  while n!=6174:
    i+=1
    a=''.join(sorted(m)); b=a[::-1]
    n=int(b)-int(a)
    m=(4-len(str(n)))*'0'+str(n)
    lst+=[(i,b,a,m)]
  return lst

