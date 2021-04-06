
def is_ascending(s):
  for i in range(1,len(s)//2+1):
    temp = [int(s[j:j+i]) for j in range(0,len(s),i)]
    if temp == list(range(min(temp),max(temp)+1)):
      return True
  return False

