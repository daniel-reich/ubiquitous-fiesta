
def replace_nums(string):
  n = ''.join([i if i.isdigit() else ' ' for i in string]).split()
  n = [d_to_b(int(i)) for i in n]
  ret = ''
  for i in range(len(string)):
    if not string[i].isdigit():
      ret+=string[i]
    elif string[i].isdigit():
      if i==0 or (i>0 and not string[i-1].isdigit()):
        ret+=n[0]
        n = n[1:]
  return ret
  
def d_to_b(n):
  ret = ''
  while n>0:
    ret+=str(n%2)
    n//=2
  return ret[::-1] if ret else '0'

