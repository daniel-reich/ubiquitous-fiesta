
def countin(txt, a):
  b=0
  for i in txt:
    if i == a:
      b += 1
  return(b)
​
def possible_palindrome(txt):
  a = 0
  for i in txt: 
    if countin(txt, i)%2 != 0:
      a += 1/countin(txt, i)
  return(a <= 1)

