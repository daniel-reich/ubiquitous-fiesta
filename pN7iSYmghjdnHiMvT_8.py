
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
    self.game = [[" " for i in range(5)] for j in range(5)]
    
  def board(self):
    alphabet = ["A","B","C","D","E"]
    
    for cord in self.scheme:
      row = alphabet.index(cord[0]) 
      col = int(cord[1]) - 1
      self.game[row][col] = "s"
      
    for guess in self.guesses:
      row = alphabet.index(guess[0]) 
      col = int(guess[1]) - 1
      if self.game[row][col] == "s":
        self.game[row][col] = "X"
      else:
        self.game[row][col] = "."
      
    return self.game
​
  def hits(self):
    j = 0
    for x in self.game:
      j += x.count("X")
    return j
​
  def sunk(self):
    alphabet = ["A","B","C","D","E","F"]
    cruisers_sunk = 0
    hits = [ship for ship in self.scheme if ship in self.guesses]
    for hit in hits:
      row = hit[0]
      col = int(hit[1])
      adjacent = [alphabet[alphabet.index(row)-1] + str(col), row + str(col+1), alphabet[alphabet.index(row)+1] + str(col), row + str(col-1)]
      for cord in adjacent:
        if cord in hits:
          cruisers_sunk += 1
    return cruisers_sunk // 2
​
  def points(self):
    count = 0
    count += self.hits()
    count += self.sunk() * 2
    return count

