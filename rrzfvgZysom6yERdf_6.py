
def player1_wins(lst):
​
  class Hand:
    
    royal_flush ='T, J, Q, K, A'.split(', ')
​
    def __init__(self, hand):
      self.hand = hand
​
      self.vals = []
      self.suits = []
      self.dic = {}
​
      for item in hand:
        try:
          self.vals.append(int(item[0]))
          value = int(item[0])
        except ValueError:
          dic = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
          if item[0] in dic.keys():
            self.vals.append(dic[item[0]])
            value = item[0]
        
        self.suits.append(item[1])
        if item[1] not in self.dic.keys():
          self.dic[item[1]] = [value]
        else:
          self.dic[item[1]].append(value)
​
      self.high_crd = max(self.vals)
​
      if len(self.suits) == 1:
        if sorted(self.dic[self.suits[0]]) == sorted(Hand.royal_flush):
          self.rf = True
        else:
          self.rf = False
      else:
        self.rf = False
      
      self.pairs = 0
      self.triple = False
      self.fourth = False
​
      for item in set(self.vals):
        c = self.vals.count(item)
        if c == 2:
          self.pairs += 1
        if c == 3:
          self.triple = True
        if c == 4:
          self.fourth = True
      
      if len(list(set(self.suits))) == 1:
        self.samesuit = True
      else:
        self.samesuit = False
      
      self.consec = False
​
      difs = []
​
      for n in range(len(self.vals)-1):
        prev = self.vals[n]
        curr = self.vals[n+1]
​
        difs.append(curr-prev)
​
      difs = list(set(difs))
      
      if len(difs) == 1 and difs[0] == 1:
        self.consec = True
      
    def versus(self, other):
      highest_card = self.high_crd
      highest_rank = 1
​
      if self.rf == True:
        highest_rank = 10
      elif self.consec == True and self.samesuit == True:
        highest_rank = 9
      elif self.fourth == True:
        highest_rank = 8
      elif self.triple == True and self.pairs == 1:
        highest_rank = 7
      elif self.samesuit == True:
        highest_rank = 6
      elif self.consec == True:
        highest_rank = 5
      elif self.triple == True:
        highest_rank = 4
      elif self.pairs == 2:
        highest_rank = 3
      elif self.pairs == 1:
        highest_rank = 2
      
      o_hc = other.high_crd
      o_highest_rank = 1
​
      if other.rf == True:
        o_highest_rank = 10
      elif other.consec == True and other.samesuit == True:
        o_highest_rank = 9
      elif other.fourth == True:
        o_highest_rank = 8
      elif other.triple == True and other.pairs == 1:
        o_highest_rank = 7
      elif other.samesuit == True:
        o_highest_rank = 6
      elif other.consec == True:
        o_highest_rank = 5
      elif other.triple == True:
        o_highest_rank = 4
      elif other.pairs == 2:
        o_highest_rank = 3
      elif other.pairs == 1:
        o_highest_rank = 2
  
      if highest_rank > o_highest_rank:
        return 1
      elif highest_rank < o_highest_rank:
        return 0
      else:
        if highest_rank == 9:
          if highest_card > o_hc:
            return 1
          elif highest_card < o_hc:
            return 0
        if highest_rank == 8:
          bi = None
          for item in set(self.vals):
            if self.vals.count(item) == 4:
              bi = item
              break
          obi = None
          for item in set(other.vals):
            if other.vals.count(item) == 4:
              obi = item
              break
          if bi > obi:
            return 1
          elif bi < obi:
            return 0
        if highest_rank == 7:
          ss = list(set(self.vals))
          os = list(set(other.vals))
​
          if max(ss) == max(os):
            if min(ss) > min(os):
              return 1
            return 0
          if max(ss) > max(os):
            return 1
          else:
            return 0
        if highest_rank == 6:
          ss = sorted(self.vals)
          os = sorted(other.vals)
​
          for n in range(1, len(ss)+1):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif s1 < oi:
              return 0
         # print(self.vals, other.vals)
          return 0
        if highest_rank == 5:
          if max(self.vals) > max(other.vals):
            return 1
          return 0
        if highest_rank == 4:
          ss = sorted(list(set(self.vals)))
          os = sorted(list(set(self.vals)))
​
          for n in range(1, len(ss)):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif s1 < oi:
              return 0
            
          #print(self.vals, other.vals)
          return 0
        if highest_rank == 3:
          pair_vals = []
          
          for item in set(self.vals):
            c = self.vals.count(item)
            if c == 2:
              pair_vals.append(item)
          
          opv = []
​
          for item in set(other.vals):
            c = other.vals.count(item)
            if c == 2:
              opv.append(item)
          
          if max(pair_vals) > max(opv):
            return 1
          elif max(pair_vals) < max(opv):
            return 0
          else:
            if min(pair_vals) > min(pair_vals):
              return 1
            elif min(pair_vals) < min(pair_vals):
              return 0
            else:
              for item in set(self.vals):
                if item not in pair_vals:
                  remaining_item = item
                  break
              for item in set(other.vals):
                if item not in opv:
                  ori = item
                  break
              
              if remaining_item > ori:
                return 1
              elif remaining_item < ori:
                return 0
              else:
                print (self.vals, other.vals)
                return 0
​
        if highest_rank == 2:
          pairval = 0
          for item in self.vals:
            c = self.vals.count(item)
            if c == 2:
              pairval = item
          ov = 0
          for item in other.vals:
            #print(item, other.vals.count(item))
            c = other.vals.count(item)
            if c == 2:
              ov = item
          
          if pairval > ov:
            return 1
          elif pairval < ov:
            return 0
          else:
            ss = sorted(list(set(self.vals)))
            os = sorted(list(set(other.vals)))
​
            for n in range(1, len(ss) + 1):
              si = ss[-n]
              oi = os[-n]
​
              if si>oi:
                return 1
              elif si < oi:
                return 0
           # print(self.vals, other.vals)
            return 0
        else:
          ss = sorted(list(set(self.vals)))
          os = sorted(list(set(other.vals)))
​
          for n in range(1, len(ss) + 1):
            si = ss[-n]
            oi = os[-n]
​
            if si > oi:
              return 1
            elif si < oi:
              return 0
          
          #print(self.vals, other.vals)
          return 0
​
​
​
  player1 = {}
  player2 = {}
  
  for n in range(len(lst)):
    ll = lst[n].split()
​
    p1 = ll[:5]
    p2 = ll[5:]
​
    player1[n] = Hand(p1)
    player2[n] = Hand(p2)
  
  p1_wins = 0
​
  for n in range(len(lst)):
    win = player1[n].versus(player2[n])
    p1_wins += win
    #print(player1[n].hand, player2[n].hand, win)
  
  return p1_wins

