
def bacteria(final_mass):
  bacterium, nights = [1], 0
  
  while sum(bacterium) < final_mass:
    temp, bacterium = bacterium, []
    
    for i in temp:
      bacterium += [i/2] + [i/2]
      
    bacterium = [i+1 for i in bacterium]
    nights += 1
    
  return nights

