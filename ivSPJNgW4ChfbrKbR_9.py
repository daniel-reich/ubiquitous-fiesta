
def soroban(frame):
  res = sum([(char == "O")* 5 * 10**i 
              for i, char in enumerate(frame[1][::-1])])
  for j in range(len(frame[3])):
    i = 3
    while frame[i][j] == "O":
      res += 10**(len(frame[3])-j-1)
      i += 1
  return res

