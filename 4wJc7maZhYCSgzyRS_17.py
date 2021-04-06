
def two_product(arr, N):
  for a in (arr[len(arr)//2:]+arr[:len(arr)//2])[::-1]:
    if a!=0 and N%a==0 and N//a in arr:
      return sorted([a,N//a], key=arr.index)

