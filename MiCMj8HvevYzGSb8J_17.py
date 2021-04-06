
def fibo_word(n):
  s="b, a, "
  a="a"
  b="b"
  c=""
  if n<2:
    return "invalid"
  for i in range(2,n):
    c=a+b
    b=a
    a=c
    if i==n-1:
      s=s+c
      return s
    else:
      s=s+c+", "

