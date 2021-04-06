
def odd_sort(lst):
  lst1 = sorted([x for x in lst if x%2], reverse=True)
  return [lst1.pop() if lst[x]%2 else lst[x] for x in range(len(lst))]

