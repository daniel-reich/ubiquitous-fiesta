
class H2O:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(hydrogen, oxygen):
    if hydrogen < 2 or oxygen < 1:
      return False
    else:
      hydrogen -= 2
      oxygen -= 1
      
      return H2O(['H', 'H', 'O']), hydrogen, oxygen
class CO2:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(carbon, oxygen):
    if carbon < 1 or oxygen < 2:
      return False
    else:
      carbon -= 1
      oxygen -= 2
      
      return CO2(['C', 'C', 'O']), carbon, oxygen
class CH4:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(carbon, hydrogen):
    if carbon < 1 or hydrogen < 4:
      return False
    else:
      carbon -= 1
      hydrogen -= 4
      
      return CH4(['C', 'H', 'H', 'H', 'H']), carbon, hydrogen
​
def chemical_reactions(carbon, hydrogen, oxygen):
  
  water = []
  carbon_dioxide = []
  methane = []
  
  water_possible = True
  carbon_dioxide_possible = True
  methane_possible = True
  
  while water_possible == True:
    wp = H2O.generate(hydrogen, oxygen)
    print(hydrogen, oxygen)
    if wp == False:
      water_possible = False
    else:
      water.append(wp[0])
      hydrogen = wp[1]
      oxygen = wp[2]
  
  while carbon_dioxide_possible == True:
    cdp = CO2.generate(carbon, oxygen)
    if cdp == False:
      carbon_dioxide_possible = False
    else:
      carbon_dioxide.append(cdp[0])
      carbon = cdp[1]
      oxygen = cdp[2]
  
  while methane_possible == True:
    mp = CH4.generate(carbon, hydrogen)
    if mp == False:
      methane_possible = False
    else:
      methane.append(mp[0])
      carbon = mp[1]
      hydrogen = mp[2]
  
  return [len(water), len(carbon_dioxide), len(methane)]

