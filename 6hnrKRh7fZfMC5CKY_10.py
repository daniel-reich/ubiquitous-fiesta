
def look_and_say(n):
  x = str(n)
  if len(x) % 2 != 0:
    return "invalid"
  num = ""
  for i,j in zip(x[::2],x[1::2]):
    num += j*int(i)
  return int(num)

