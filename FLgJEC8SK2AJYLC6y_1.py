
class Room:
  
  def __init__(self, rid, connected = []):
    self.rid = rid
    self.con = connected = []
  
  def can_move(self, other):
    return other in self.con
  
  def add_connections(self, connections):
    self.con += connections
    return True
​
school = {1: Room(1), 2: Room(2), 'H': Room('H'), 3: Room(3), 4: Room(4)}
​
school[1].add_connections([school[2]])
school[2].add_connections([school[1], school['H']])
school['H'].add_connections([school[2], school[4]])
school[3].add_connections([school[4]])
school[4].add_connections([school[3], school['H']])
​
def possible_path(lst):
  
  for n in range(len(lst) - 1):
    cr = lst[n]
    nr = lst[n+1]
    
    move = school[cr].can_move(school[nr])
    
    if move == False:
      print(n)
      return False
      print(n)
  
  return True

