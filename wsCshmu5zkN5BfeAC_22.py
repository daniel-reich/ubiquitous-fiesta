
def divisible_by_left(n):
  arr = [int(x) for x in list(str(n))]
  return [False]+[arr[y+1]%x==0 if x!=0 else False for y,x in enumerate(arr) if y<len(arr)-1]

