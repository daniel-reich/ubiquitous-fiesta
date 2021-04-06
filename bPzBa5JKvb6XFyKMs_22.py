
def get_primiera_score(deck):
 suit_lst=['d','h','c','s']
 point_scale={'A':16,'2':12,'3':13,'4':14,'5':15,'6':18,'7':21,'J':10,'Q':10,'K':10}
 points=0
 # go through suits
 for suit in suit_lst:
  #print('suit ',suit)
  # go through deck
  #   find best card
  best=0
  for i in range(0,len(deck)):
   card=0
   # define card val 
   if deck[i][1] == suit:
    card=point_scale[deck[i][0]]
   # is card val higher then best
   if card > best:
    best=card
  #print('best ',best)
  # add best val to points
  if best != 0:
   points+=best
  else:
   return 0
 return points

