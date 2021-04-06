
def briscola_score(my_deck1, my_deck2):
  s1=0
  s2=0
  s={
    'A':11,
    '2':0,
    '3':10,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    'K':4,
    'Q':3,
    'J':2
  }
  for i in range(0,len(my_deck1)):
    s1=s1+s.get(my_deck1[i][0])
  for j in range(0,len(my_deck2)):
    s2=s2+s.get(my_deck2[j][0])
  if(s1+s2==120):
    return "Draw!"
  elif(s1+s2>120):
    return "You Win!"
  else:
    return "You Lose!"

