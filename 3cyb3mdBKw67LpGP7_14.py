
def numbers_need_friends_too(m):
  qq=str(m)
  n=[int(i) for i in qq]
  index=[]
  for i in range(0,len(n)-1):
    if n[i] != n[i+1]:
      index.append(i)     
  index= [x+1 for x in index]
  final_lst=[]
  for i,j in zip([0]+index,index+[None]):
    if len(n[i:j])<2:
      temp_lst=n[i:j]+n[i:j]+n[i:j]
    else:
      temp_lst=n[i:j]
    final_lst.extend(temp_lst)
  qqq=[str(i) for i in final_lst]
  a_a="".join(qqq)
  return int(a_a)

