
class Bacteria_Colony:
  
  def __init__(self, num_of_bact, bact_mass):
    self.nob = num_of_bact
    self.bm = bact_mass
    self.tm = self.nob * self.bm
  
  def grow(self):
    self.bm += 1
    self.tm = self.nob * self.bm
    return True
  
  def split(self):
    self.nob *= 2
    self.bm = self.bm / 2
    self.tm = self.nob * self.bm
    return True
    
​
def bacteria(final_mass):
  
  colony = Bacteria_Colony(1, 1)
  previous_mass = 0
  nights = 0
  
  while colony.tm < final_mass:
    if colony.tm > previous_mass:
      previous_mass = colony.tm
      colony.split()
    # print('split')
    colony.grow()
    nights += 1
    #print(colony.nob, colony.bm, colony.tm)
  
  return nights

