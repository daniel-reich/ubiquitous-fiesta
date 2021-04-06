
def divide(lst, n):
  i = 0
  s = 0
  chunks = []
  chunk = []
  while i < len(lst):
    s += lst[i]
    chunk.append(lst[i])
    if s > n:
      s = lst[i]
      chunks.append(chunk[:-1])
      chunk = [lst[i]]
    i += 1
  chunks.append(chunk)
  return chunks

