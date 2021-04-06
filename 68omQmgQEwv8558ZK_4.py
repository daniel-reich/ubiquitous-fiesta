
ch = {  'Knight' :  [120 , 140 , 6] , 'Warrior': [180 , 71 , 8] ,
    'Fairy' :   [71 , 100 , 16] , 'Robot':  [160 , 120 , 11], 
    'Giant' :   [160 , 200 , 4] }
​
shops = [{(10 , 20), (20 , 40), (30 , 60), (40 , 80), (50 , 100)},
    {(20 , 30), (40 , 60), (60 , 90), (80 , 120), (100 , 150)},
    {(3 , 24), (6 , 48), (9 , 72), (12 , 96), (15 , 120)}]
​
def max_stats(c, g):
  best = lambda store: max(i for i in store if i[1] <= g)[0]
  return [ch[c][x] + best(shops[x]) for x in range(3)]

