
def fibo_word(n):
  if n < 2: return 'invalid'
  if n == 2: return 'b, a'
  return (fibo_word(n-1) + ', ' 
         + ''.join(fibo_word(n-1).split(', ')[-2::][::-1]))

