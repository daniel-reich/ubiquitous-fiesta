
def longest_palindrome(s):
  d = dict([[i,s.count(i)] for i in s])
  ret = 0
  for i in d:
    if ret==0 and any([d[j]%2==1 for j in d]):
      ret+=1
    if d[i]>=2:
      ret+=(d[i]//2)*2
  return ret if s else 0

