
def closest_palindrome(n):
  i,p=0,lambda m:str(m)==str(m)[::-1]
  while 1:
    if p(n-i): return n-i
    if p(n+i): return n+i
    i+=1

