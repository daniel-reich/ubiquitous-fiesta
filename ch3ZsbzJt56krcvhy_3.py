
def square_root(n):
  start = 1
  end = n
  if n == 0 or n == 1:
    return n
  while start <= end:
    mid = (start+end)//2
    if mid*mid == n:
      return mid
    elif mid*mid < n:
      start = mid+1
    else:
      end = mid-1

