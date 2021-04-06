
def is_ascending(s):
  for i in range(1,len(s)):
    if len(s)%i==0:
      groups = [s[j:j+i] for j in range(0,len(s),i)]
      if all(int(groups[j])+1==int(groups[j+1]) for j in range(len(groups)-1)):
        return True
  return False

