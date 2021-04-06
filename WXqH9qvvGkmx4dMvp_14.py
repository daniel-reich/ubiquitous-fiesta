
def fizz_buzz(num):
  s=''
  if not num%3: s+='Fizz'
  if not num%5: s+='Buzz'
  if s: return s
  else: return str(num)

