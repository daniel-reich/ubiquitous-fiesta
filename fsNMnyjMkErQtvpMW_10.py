
def holes(n):
  return sum(
    1 if i in '4690' else 2 if i in '8' else 0
    for i in str(n)
  )
​
​
def holey_sort(lst):
  return sorted(lst, key=holes)

