
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
  #Rules
  #2 Types of Ships: Patrol or Cruiser
    #Patrol = 1 Spot
    #Cruiser = 2 Spots H/V
  #3 Patrols 3 Cruisers randomly on Board 
  #Player calls 6 guesses
  #For hit, player gets 1 point, for cruiser sunk, player gets 2 extra points
  
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
​
    spaces = []
​
    for l8r in sorted(list('ABCDE')):
      for num in range(1, 6):
        spaces.append('{}{}'.format(l8r,num))
    
    self.spaces = {}
    self.hitts = 0
    for space in spaces:
      if space in self.scheme:
        if space in self.guesses:
          self.spaces[space] = 'X'
          self.hitts += 1
        else:
          self.spaces[space] = 's'
      else:
        if space in self.guesses:
          self.spaces[space] = '.'
        else:
          self.spaces[space] = ' '
    
    self.cruisers = []
    already_found = []
    self.score = self.hitts 
​
    for guess in self.guesses:
      print(guess)
      if guess in already_found:
        #print(guess)
        continue
      elif self.spaces[guess] == '.' or self.spaces[guess] == ' ':
        continue
      else:
        if l8r == 'D':
          print ('LHLjd')
        possible_next = []
        l8rs = 'ABCDE'
        nums = [str(i) for i in range(1, 6)]
​
        l8r = guess[0]
        num = guess[1]
​
        if l8r == 'A':
          poss_l8rs = ['B']
        elif l8r == 'E':
          poss_l8rs = ['D']
        else:
          index = None
          for n in range(len(l8rs)):
            tl8r = l8rs[n]
            if tl8r == l8r:
              index = n
              break
          poss_l8rs = [l8rs[n-1], l8rs[n+1]]
      
        if num == '1':
          poss_nums = ['2']
        elif num == '5':
          poss_nums = ['4']
        else:
          poss_nums = [str(int(num) - 1), str(int(num) + 1)]
      
        for pl8r in poss_l8rs:
          possible_next.append('{}{}'.format(pl8r, num))
        for pnum in poss_nums:
          possible_next.append('{}{}'.format(l8r, pnum))
        if l8r == 'D':
          print(guess, possible_next, 'hi')
        #print(guess, possible_next)
        for spot in possible_next:
          if spot in already_found:
            continue
          elif self.spaces[spot] == 'X':
            self.cruisers.append(False)
            already_found.append(spot)
            already_found.append(guess)
            print(guess, spot, False)
          elif self.spaces[spot] == 's':
            self.cruisers.append(True)
            already_found.append(spot)
            already_found.append(guess)
            print(guess, spot, True)
    
    for cruiser in self.cruisers:
      if cruiser == False:
        self.score += 2
​
  def board(self):
​
    l8rs = 'ABCDE'
    nums = [str(i) for i in range(1,6)]
​
    brd = []
​
    for l8r in l8rs:
      row = []
      for num in nums:
        row.append(self.spaces['{}{}'.format(l8r, num)])
      brd.append(row)
    
    return brd
  
  def hits(self):
    return self.hitts
    
  def sunk(self):
    return len([s for s in self.cruisers if s == False])
  
  def points(self):
    return self.score

