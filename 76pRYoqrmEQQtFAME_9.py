
def is_astonishing(num):
  num = str(num)
  for i in range(1,len(num)):
    a,b = int(num[:i]),int(num[i:])
    if a < b:
      if s(a,b)==int(num):
        return 'AB-Astonishing'
    else:
      if s(b,a)==int(num):
        return 'BA-Astonishing'
  return False
  
def s(a,b):
  return sum([i for i in range(a,b+1)])

