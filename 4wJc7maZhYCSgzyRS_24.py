
def two_product(arr, N):
  brr = []
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]*arr[j] == N:
        brr.append([abs(j-i),[arr[i],arr[j]]])
  if len(brr) > 0:
    return sorted(brr)[0][1]
  else : return None

