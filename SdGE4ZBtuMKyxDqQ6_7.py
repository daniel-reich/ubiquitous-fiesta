
def first_repeat(chars):
  count=0
  for i in range(0,len(chars)):
    if chars[i+1:].count(chars[i]) > 0:
        return chars[i]
        break
    else:
      count+=1
  if count == len(chars):
    return "-1"

