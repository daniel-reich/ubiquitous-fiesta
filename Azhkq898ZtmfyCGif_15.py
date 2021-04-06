
def numbers_to_ranges(lst):
  if not lst: return lst
  string = str(lst[0])
​
  if len(lst) == 1:
    return [str(lst[0])]
  
  for x in range(1, len(lst)):
    if lst[x-1] + 1 != lst[x]:
      if string[-1] == str(lst[x-1]):
        string += ' ' + str(lst[x])
        continue
      string += '-' + str(lst[x-1])
      string += ' ' + str(lst[x])
​
​
​
  string += '-' + str(lst[x])
  return string.split()

