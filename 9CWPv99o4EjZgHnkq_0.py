
def divide(lst, n):
  chunks,x=[],0
  for i in range(1,len(lst)):
    if sum(lst[x:i+1])>n:
      chunks.append(lst[x:i])
      x=i
  chunks.append(lst[x:])
  return chunks

