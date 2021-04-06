
def max_possible(n1, n2):
  second = str(n2)
  first = str(n1)
  maxnum = ""
  for num in first:
    if second == "":
      maxnum += num
    elif num < max(second):
      maxnum += max(second)
      second = second.replace(max(second),"",1)
    else:
      maxnum += num
  return int(maxnum)

