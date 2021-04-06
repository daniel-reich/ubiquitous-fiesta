
def odd_sort(lst):
  even = [i for i in lst if i%2 == 0][::-1]
  odd = sorted([i for i in lst if i%2], reverse=True)
  out = []
  for i in range(len(lst)):
    if lst[i] % 2:
      out.append(odd.pop())
    else:
      out.append(even.pop())
  return out

