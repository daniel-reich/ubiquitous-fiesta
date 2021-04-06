
def same_length(txt):
  if len(txt) % 2 or txt[-1] == "1":
    return False
  ones = 0
  counter = 0
  while counter >= len(txt):
    if txt[counter] == "1":
      ones += 1
    elif "1" in txt[counter:counter + ones]:
      return False
    else:
      counter += ones
      ones = 0
    counter += 1
  return True

