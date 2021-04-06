
def num_grid(lst):
  a=len(lst)
  b=len(lst[0])
  out=lst
  for x in range(0,a):
    for y in range(0,b):
      if lst[x][y] == "-":
        out[x][y]=0
        for xx in [-1,0,1]:
          for yy in [-1,0,1]:
            if x+xx<0 or x+xx>a-1 or y+yy<0 or y+yy>b-1:
              1
            else:
              if lst[x+xx][y+yy]=="#":
                out[x][y] = out[x][y] + 1
        out[x][y]=str(out[x][y])
  return out

