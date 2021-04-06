
def remove_leading_trailing(n):
  n = n.split(".")
  left = n[0]
  while left[0] == "0":
    if int(n[0]) == 0 and len(n) == 2 and int(n[1]) != 0:
      left = "0"
      break
    elif int(n[0]) == 0:
      return "0"
    else:
      left = left[1:]
  if len(n) == 2 and int(n[1]) != 0:
    right = n[1]
    right = right[::-1]
    while right[0] == "0":
      right = right[1:]
    right = right[::-1]
    result = left+"."+right
    return result
  else:
    return left

