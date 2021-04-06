
def mixed_number(n):
  n = [int(i) for i in n.split('/')]
  g = gcd(abs(n[0]),abs(n[1]))
  g1 = gcd((n[0]%n[1]),n[1])
  if n[0]==0:return '0'
  if abs(n[0]) < abs(n[1]):return str(n[0]//g) +'/'+ str(n[1]//g)
  if n[0]%n[1]==0:return str(n[0]//n[1])
  if n[0] < 0 :return '-' + str(abs(n[0])//n[1]) +' '+ str(abs(n[0])%n[1]//g1) + '/' + str(n[1]//g1)
  return str(abs(n[0])//n[1]) +' '+ str(abs(n[0])%n[1]//g1) + '/' + str(n[1]//g1)         
​
def gcd(a,b): 
  if(b==0): 
    return a 
  else: 
    return gcd(b,a%b)

