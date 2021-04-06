
def extend_vowels(word, num):
  if num<0 or isinstance(num,float): return 'invalid'
  ans=''
  for i in word:
    if i in "AEIOUaeiou":ans+=i*(num+1)
    else: ans+=i
  return ans

