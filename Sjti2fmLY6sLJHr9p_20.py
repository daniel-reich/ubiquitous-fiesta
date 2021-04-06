
def look_and_say(start, n):
  lst = [start]
  while len(lst)<n:
    lst.append(read_int(lst[-1]))
  return lst
    
def read_int(i):
  i = str(i)
  j = i[0]
  for x in range(1,len(i)):
    if i[x]!=i[x-1]:
      j+=' '+i[x]
    else:
      j+=i[x]
  j = ''.join([str(len(x))+x[0] for x in j.split()])
  return int(j)

