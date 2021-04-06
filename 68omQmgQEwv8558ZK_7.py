
def max_stats(character, gold):
    char = {'Knight': [120, 140, 6], 'Warrior': [180, 71, 8], 'Fairy': [71, 100, 16],
         'Robot': [160, 120, 11], 'Giant': [160, 200, 4]}
    item = [min(10*(gold//20), 50), min(20*(gold//30), 100), min(3*(gold//24), 15)]
    return list(map(lambda x,y: x+y, char[character], item))

