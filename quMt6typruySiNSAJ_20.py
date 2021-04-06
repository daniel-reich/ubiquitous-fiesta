
def shuffle_count(num):
  og = list(range(1,num+1))
  cur = og[:]
  count = 0
  while count==0 or og!=cur:
    count+=1
    temp = []
    for i in range(num//2):
      temp.append(cur[i])
      temp.append(cur[i+num//2])
    cur = temp
  return count

