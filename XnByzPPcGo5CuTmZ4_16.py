
def kix_code(addr):
  p=',-/'
  lst=addr.split(",")
  s1=(lst[-1][:8]).replace(' ','')
  l2=lst[1].split(' ')
  for i in l2:
    if i.isnumeric():
      break
  s2=(','.join(l2[l2.index(i):])).upper()
  for i in p:
    if i in s2:
      s2=s2.replace(i,'X')
  return s1+s2

