
def largest_gap(lst):
  lst = sorted(lst)
  arr = []
  for i in range(len(lst)-1):
    arr.append(abs(lst[i]-lst[i+1]))
  return max(arr)

