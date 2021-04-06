
def knights_jump(square):
  letter = ord(square[0])
  number = int(square[1])
  strings = []
  for num in [-2,-1,1,2]:
    if number + num > 0 and number+num <= 8:
      for l in [-2,-1,1,2]:
        if letter + l >= 65 and letter + l <= 72 and abs(num) != abs(l):
          strings.append(chr(l+letter)+str(number+num))
  return ','.join(strings)

