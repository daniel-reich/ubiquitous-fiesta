
def overlapping_rectangles(rect1, rect2):
  a=[(rect1[0]+i,rect1[1]+j)for j in range(rect1[3]+1) for i in range(rect1[2]+1)]
  b=[(rect2[0]+i,rect2[1]+j)for j in range(rect2[3]+1) for i in range(rect2[2]+1)]
  if set(a)&set(b):
    c=set(a)&set(b)
    x=max([i[0]for i in c])-min([i[0]for i in c])
    y=max([i[1]for i in c])-min([i[1]for i in c])
    return (x*y)
  else:
    return 0

