
def hex_lattice(n):
  side, hexn = 1,1
  while hexn <= n:
    if hexn == n:
      return "\n".join([blobs(i,side) for i in range(side,2*side)]+[blobs(3*side-2-i,side) for i in range(side,2*side-1)])
    side +=1
    hexn += 6*(side-1)
  return "Invalid"
​
def blobs(count,side):
  return " "*(2*side - count) + " ".join(["o"]*count) + " "*(2*side - count)

