
def check(l):
  tmp = 0
  for i in range(len(l)):
    if l[i][1] == False:
      tmp += 1
  if tmp == 1:
    return True
  else:
    return False
    
def josephus(n):
  if n == 0:
    return 0
  data = [[i,False] for i in range(n)]
  pos = 0
  switch = False
  while not check(data):
    if not switch:
      if data[pos][1] == False:
        switch = True
    else:
      if data[pos][1] == False:
        switch = False
        data[pos][1] = True
    pos += 1
    if pos == len(data):
      pos = 0
  for i in data:
    if i[1] == False:
      return i[0]

