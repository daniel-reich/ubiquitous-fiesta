
def divide(lst, n):
  nums = []
  try:
    while len(lst) > 0:
      current = []
      current.append(lst[0])
      lst.pop(0)
      while True:
        if lst[0] + sum(current) > n:
          nums.append(current)
          break
        current.append(lst[0])
        lst.pop(0)
  except IndexError:
    nums.append(current)
    return nums

