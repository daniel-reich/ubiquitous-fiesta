
def josephus(people):
  f=bin(people)
  return b(f[3:]+f[2])
def b(n):
  s=0
  for i in range(0,len(n)):
    s+=int(n[i])*(2**(len(n)-i-1))
  return s

