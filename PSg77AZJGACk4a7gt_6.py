
def meme_sum(a, b):
  sum = ""
  c=0
  if b>a:
      c=a
      a=b
      b=c
  a = str(a)
  b= str(b)  
  i=0
  while i < (len(a)-len(b)):
    sum = sum + a[i]
    i += 1
  i = 0
  while i < len(b):
    sum = sum + str((int(a[i+len(a)-len(b)])+ int(b[i])))
    i += 1
  return int(sum)

