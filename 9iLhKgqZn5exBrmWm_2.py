
def ascending(txt):
  n=1
  while n<len(txt)/2+1:
    chunks = [int(txt[i:i+n]) for i in range(0,len(txt),n)]
    if all(chunks[j]-chunks[j-1]==1 for j in range(1,len(chunks))):
      return True
    n+=1
  return False

