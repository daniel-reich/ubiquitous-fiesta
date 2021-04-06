
def is_unprimeable(num):
  num=str(num);res=[]
  for i in range(len(num)):
    for j in range(10):
      mem=int(num[:i]+str(j)+num[i+1:])
      if is_prime(mem):res+=[mem]
  return 'Prime Input' if is_prime(int(num)) else 'Unprimeable' if res==[] else sorted(res)
  
def is_prime(num):
  if num in [0,1]:return False
  return all([num%i for i in range(2,num//2+1)])

