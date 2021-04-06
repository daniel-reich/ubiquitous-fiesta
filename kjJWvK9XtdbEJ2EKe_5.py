
def sort_array(arr):
  MIN,MAX = min(arr),max(arr)
  lst = [0] * (MAX-MIN+1)
  for k in arr:
    lst[k-MIN] = 1
  return [i+MIN for i in range(len(lst)) if lst[i]]

