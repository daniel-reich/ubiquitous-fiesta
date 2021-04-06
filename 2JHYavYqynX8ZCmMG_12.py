
def get_total(str):
    total = 0
    for char in str:
        total += ord(char)
​
    return total
​
def ascii_sort(lst):
  min_total = get_total(lst[0])
  min_str = lst[0]
  for str in lst:
    if min_total > get_total(str):
      min_total = get_total(str)
      min_str = str
  return min_str

