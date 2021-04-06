
def is_consecutive(s):
  size = len(s)
  for value in range(1, size//2 + 1):
    index = 0
    num = int(s[index:index+value])
    index += value
    asc = True
    while index < size:
      temp = int(s[index:index+value])
      if index-value == 0:
        if num - 1 == temp:
          asc = False
        elif num + 1 == temp:
          asc = True
        else:
          break
      else:
        if asc:
          if num + 1 != temp:
            break
        else:
          if num - 1 != temp:
            break
      index += value
      num = temp
    else:
      return True
  return False

