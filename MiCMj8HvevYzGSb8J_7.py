
def fibo_word(n):
  if n<2: return 'invalid'
  ans = ['b','a']
  for i in range(2,n):
    ans.append(ans[-1]+ans[-2])
  return ', '.join(ans)

