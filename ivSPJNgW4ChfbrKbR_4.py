
def soroban(frame):
  upper_deck = 0
  lower_deck = 0
  
  #calc upper deck -> the EZ part
  for i in range(0,len(frame[1])):
    if frame[1][i] == 'O':
      p = 10**(len(frame)-i-2)
      upper_deck += p * 5
      
  #calc lower deck
  for i in range(0,len(frame[3])):
    if frame[3][i] == 'O':
      print("expand col : " + str(i))
      c = 3
      q = 0
      while(frame[c][i] == 'O'):
        c += 1
        q += 1
      print(q)
      p = 10**(len(frame)-i-2) * q
      lower_deck += p * 1
  return upper_deck + lower_deck

