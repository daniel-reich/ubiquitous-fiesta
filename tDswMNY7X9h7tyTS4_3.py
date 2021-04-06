
def pascals_triangle(n):
  trow, ans = [1], [1]
  y = [0]
  
  for x in range(1, n):
    trow=[left+right for left,right in zip(trow+y, y+trow)]
    for i in trow:
      ans.append(i)
  
  return ans

