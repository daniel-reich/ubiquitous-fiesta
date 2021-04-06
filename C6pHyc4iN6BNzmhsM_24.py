
order = list(range(2, 11))
order = [str(i) for i in order]
pics = ['J', 'Q', 'K', 'A']
order+= pics
​
order += order
def poker_hand_ranking(deck):
​
  lst = deck
    
  suit_dic = {}
  num_dic = {}
    
    
  for c in lst:
    
        
    if c[-1] not in suit_dic.keys():
            
      suit_dic[c[-1]] = 1
        
    else:
            
      suit_dic[c[-1]] += 1
            
    if c[:-1] not in num_dic.keys():
            
      num_dic[c[:-1]] = 1
        
    else:
            
      num_dic[c[:-1]] += 1
     
    
  num_lst = list(num_dic.values())
  flush = 5 in suit_dic.values()
    
  fh = 3 in num_dic.values() and 2 in num_dic.values()
    
  hc = max(num_dic.values()) == 1
  op = max(num_dic.values()) == 2
  tk = max(num_dic.values()) == 3
  fk = max(num_dic.values()) == 4
    
  tp_count = sum([1 for i in num_lst if i == 2])
    
  tp = tp_count > 1     
    
    
  perms = []
    
    
  lst2 = [i[:-1] for i in lst]
    
  from itertools import permutations
    
  for i in range(0, len(lst2)+1):
    for subset in permutations(lst2, i):
      if len(subset) == 5:
        perms.append(list(subset))
​
    
    
    
  straight = False
    
  for i in range(len(order)):
        
    if order[i: i+5] in perms:
            
      straight = True
      break
    
  lst3 = [i[:-1] for i in lst]
    
  if straight == True and flush == True and 'A' in lst3 and 'K' in lst3 and 'Q' in lst3 and 'J' in lst3 and '10' in lst3:
        
    return 'Royal Flush'
    
  elif straight == True and flush == True:
    return 'Straight Flush'
    
  elif fk == True:
    return 'Four of a Kind'
    
  elif fh == True:
    return 'Full House'
    
  elif flush == True:
    return 'Flush'
    
  elif straight == True:
    return 'Straight'
    
  elif tk == True:
    return 'Three of a Kind'
    
  elif tp == True:
    return 'Two Pair'
    
  elif op == True:
    return 'Pair'
    
  else:
    return 'High Card'

