
def soroban(frame):
  global_count = 0
  for i in range(0,7):
    count = 0
    if frame[0][i] == "|":
      count += 5
    n=3
    while frame[n][i].lower() == 'o':
      count +=1
      n+=1
  
    global_count += 10**(6-i)*count
  
  return global_count

