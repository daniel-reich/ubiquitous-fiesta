
def verif(n,b):
  r=''
  while n: r+=str(n%b) ; n//=b
  return all([abs(int(r[i-1])-int(r[i]))==1 for i in range(1,len(r))])
​
def esthetic(num):
  r = [i for i in range(2,11) if verif(num,i)]
  return r if r else 'Anti-Esthetic'

