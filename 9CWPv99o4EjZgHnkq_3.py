
def divide(lst, n):
  chunks = []
  temp = []
  for i in range(len(lst)):
    temp.append(lst[i])
    if sum(temp) > n:
      chunks.append(temp[:-1])
      temp = [temp[-1]]
      
  if sum(temp) > n:
    chunks.append(temp[:-1])
    chunks.append(temp[-1])
  else:
    chunks.append(temp)
  return chunks

