
def divide(lst, n):
  def divide(lst, n):
    chunk = []
    index = 0
​
    while sum(chunk) <= n and index < len(lst):
      chunk.append(lst[index])
      index += 1
      
    if sum(chunk) > n:
      chunk.pop(-1)
    
    if chunk == lst:
      return chunk, []
    
    for n in range(len(chunk)):
      lst.pop(0)
    
    return chunk, lst
  
  chunks = []
  c = 0
​
  while len(lst) > 0 and c < 1000:
    d = divide(lst, n)
    chunks.append(d[0])
    lst = d[1]
​
  return chunks

