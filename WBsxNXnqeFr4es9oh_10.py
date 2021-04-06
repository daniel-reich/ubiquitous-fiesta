
def clockwise_cipher(message):
  length = 0
  while length*length<len(message):
    length+=1
  clock = [[' ' for c in range(length)] for r in range(length)]
  ring = 0
  x,y = 0,0
  direct = 'urdl'
  side = 'u'
  for i in range(len(message)):
    clock[x][y] = message[i]
    if side=='l' and x-ring-1==0:
      ring+=1
      x = ring
      y = ring
    elif side=='u':
      x = y
      y = length-1-ring
    elif side=='r':
      y = length-x-1
      x = length-1-ring
    elif side=='d':
      x = y
      y = ring
    else:
      y = length-x
      x = ring
    side = direct[(direct.find(side)+1)%4]
  return ''.join(''.join(r) for r in clock)

