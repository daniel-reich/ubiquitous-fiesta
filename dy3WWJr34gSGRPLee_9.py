
def makeBox(n):
  if n == 1:
    return ["#"]
  end = "#" * n
  middle = "#" + (" " * (n-2)) + "#"
  box = [end]
  for i in range(2, n):
    box.insert(i, middle) 
  box.append(end)
  return box

