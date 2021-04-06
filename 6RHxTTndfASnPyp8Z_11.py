
def compress(chars):
  chars = "".join(chars) + " "
  result = ""
  count = 0
  for i, l in enumerate(chars):
    if i == 0:
      count += 1
    else:
      if l != chars[i-1]:
        if count == 1:
          result += chars[i-1]
        else:
          result += chars[i-1] + str(count)
        count = 1
      else:
        count += 1
  return result

