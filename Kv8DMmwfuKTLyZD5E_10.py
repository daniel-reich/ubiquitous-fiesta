
def make_dartboard(n):
  if n == 1:
    return [1]
  if n == 2:
    return [11,11]
  
  lines =["1"*n]
  for i in range(1,n//2+1):
    lines.append(lines[-1][:i] + "".join(list(map(lambda x: str(int(x)+1),lines[-1][i:-i]))) + lines[-1][-i:])
  if n%2 == 1:
    lines.extend(lines[:-1][::-1])
  else:
    lines.extend(lines[:-2][::-1])
  return list(map(int,lines))

