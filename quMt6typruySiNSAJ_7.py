
def shuffle_count(num):
  orig = [i for i in range(1,num+1)]
  ret = 1
  lst = zp(orig)
  while lst!=orig:
    lst = zp(lst)
    ret+=1
  return ret
  
def zp(lst):
  a,b = lst[:len(lst)//2],lst[len(lst)//2:]
  ret = []
  for i in range(len(a)):
    ret.append(a[i])
    ret.append(b[i])
  return ret

