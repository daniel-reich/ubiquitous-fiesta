
def shuffle_count(num):
  ret = 1
  lst = list(range(1,num+1))
  a,b = lst[:len(lst)//2],lst[len(lst)//2:]
  lst = []
  for i in range(len(a)):
    lst+=[a[i]]+[b[i]]
  while lst!=list(range(1,num+1)):
    ret+=1
    a,b = lst[:len(lst)//2],lst[len(lst)//2:]
    lst = []
    for i in range(len(a)):
      lst+=[a[i]]+[b[i]]
  return ret

