
def freed_prisoners(prison):
  if prison[0] == 0:
    return(0)
  count = 1
  for i in range(1, len(prison)):
    if prison[i] != prison[i-1]:
      count+=1
  return(count)

