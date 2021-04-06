
def overlapping_rectangles(rect1, rect2):
  def length(i,j):
    rects = sorted([rect1,rect2],key = lambda x: x[i])
    a,b = rects[0],rects[1]
    k1,k2,k3,k4 = a[i],a[i] + a[j],b[i],b[i] + b[j]
    if k2 < k3:
      return 0
    if k4 <= k2:
      return k4 - k3
    return k2 - k3
  return length(0,2) * length(1,3)

