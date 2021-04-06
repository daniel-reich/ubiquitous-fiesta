
def sock_pairs(socks):
 sock_set=set(socks)
 #print(sock_set)
 pairs=0
 for sock in sock_set:
  count=0
  for i in range(0,len(socks)):
   if socks[i] == sock:
    count+=1
  if count // 2 > 0:
   pairs+=int(count//2)
 return pairs

