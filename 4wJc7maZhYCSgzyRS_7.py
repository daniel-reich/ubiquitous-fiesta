
def two_product(arr, N):
  
  nl = []
​
  for num in arr:
    if num and not N%num and N//num in arr:
      nl.append( [num, N//num, abs(arr.index(num)-arr.index(N//num)) ] )
​
  nl = sorted(nl,key=lambda x: x[-1])
​
  return None if not nl else nl[0][:2]

