
count = 0
​
def look_and_say(start, n):
  global count
  if n == 1:
    count = 0
    return []
  number = str(start)
  lst = []
  current = number[0]
  for idx, digit in enumerate(number[1:]):
    if number[idx] == digit:
      current += digit
    else:
      lst.append(current)
      current = digit
  if current != "":
    lst.append(current)
  new = int("".join([str(len(i)) + i[0] for i in lst]))
  if count == 0:
    count += 1
    return [start, new] + look_and_say(new, n-1)
  return [new] + look_and_say(new, n-1)

