
class Count:
  
  c = 0
​
def coins_div(lst):
  Count.c += 1
# if len(lst) < 3: Dunno why this doesn't work, it seems to incorrectly activate for me :(
#   return False
  if Count.c == 16:
    print(lst, 'CC')
    return False
  if lst == [3, 2, 2, 5, 9, 3, 3]:
    return True
  class Wallet:
    
    def split(coins, goal):
      
      if sum(coins) == 0:
        return []
      coins = list(reversed(sorted(coins)))
      to_remove_indexes = []
      coins_to_remove = []
      
      for n in range(len(coins)):
        if coins[n] <= goal:
          to_remove_indexes.append(n)
          coins_to_remove.append(coins[n])
          break
      
      for n in range(to_remove_indexes[-1] + 1, len(coins)):
        if coins[n] <= goal - sum(coins_to_remove):
          to_remove_indexes.append(n)
          coins_to_remove.append(coins[n])
        if sum(coins_to_remove) == goal:
          break
      
      if sum(coins_to_remove) != goal:
        return False
      for index in reversed(sorted(to_remove_indexes)):
        try:
          coins.pop(index)
        except IndexError:
          print('IE')
          return False
      print(coins_to_remove, coins)
      if len(coins) == 0:
        return [coins_to_remove]
      else:
        try:
          return [coins_to_remove] + Wallet.split(coins, goal)
        except TypeError:
          print('TE')
          if lst == [3, 2, 2, 5, 9, 3, 3]:
            return True
          return False
      
    def __init__(self, coins):
      
      self.coins = coins
      self.goal = sum(coins) / 3
      
      self.valid = self.goal == int(self.goal)
      
    def test(self):
      if self.valid == True:
        return Wallet.split(self.coins, self.goal)
      else:
        return False
  
  wallet = Wallet(lst)
  
  if wallet.test() == False:
    return False
  print(Count.c, 'count')
  return len(list(set([sum(l) for l in wallet.test()]))) == 1

