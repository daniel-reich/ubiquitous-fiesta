
def shuffle_count(num):
  arr=[x for x in range(1, num+1)]
  A=[]
  while arr not in A:
    A.append(arr)
    arr=[c for x in zip(arr[:num//2], arr[num//2:]) for c in x]
  return len(A)

