
def is_consecutive(s):
  for i in range(1,len(s)//2+1):
    tmp = [int(s[j:j+i]) for j in range(0,len(s),i)]
    if all(b-a==1 for a,b in zip(tmp,tmp[1:])) or all(b-a==1 for b,a in zip(tmp,tmp[1:]) ):
      return True
  return False

