
def max_stats(character, gold):
  stats = {'K': [120, 140, 6], 'W': [180, 71, 8], 
       'F': [71, 100, 16], 'R': [160, 120, 11], 
       'G': [160, 200, 4]}[character[0]]
       
  weapon = next(i for i in [50, 40, 30, 20, 10, 0] if i*2 <= gold)
  armor = next(i for i in [100, 80, 60, 40, 20, 0] if i*1.5 <= gold)
  boots = next(i for i in [15, 12, 9, 6, 3, 0] if i*8 <= gold)
  
  return [a+b for a, b in zip(stats, [weapon, armor, boots])]

