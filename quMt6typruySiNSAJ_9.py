
def shuffle_count(num):
  def is_same(a,b):
    for (x,y) in zip(a,b):
      if x != y:
        return False
    return True
    
  def shuffle(deck):
    a = deck[:int(len(deck)/2)]
    b = deck[int(len(deck)/2):]
    ret = []
    
    for (x,y) in zip(a,b):
      ret.append(x)
      ret.append(y)
      
    return ret
  
  orig_deck = range(1, num+1)
  mut_deck = [x for x in orig_deck]
  
  iters = 0
  while(True):
    mut_deck = shuffle(mut_deck)
    iters += 1
    if is_same(orig_deck, mut_deck):
      return iters

