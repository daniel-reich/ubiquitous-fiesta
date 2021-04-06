
def same_length(txt):
  up = True
  count = 0
  for i in txt:
    if up and i == "1":
      count += 1
    if i == "0":
      up = False
      count -= 1
    if not up and i == "1":
      if count == 0:
        up = True
        count += 1
      else:
        break
  return count == 0

