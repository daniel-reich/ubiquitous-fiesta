
def is_zygodrome(num):
  n = str(num)
  if len(n)<2 or n[0] != n[1] or n[-1] != n[-2]: return False
  return all(n[i]==n[i-1] or n[i]==n[i+1] for i in range(1,len(n)-1))

