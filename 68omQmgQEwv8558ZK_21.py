
def buy_best(gold):
    weapons = ((100, 50), (80, 40), (60, 30), (40, 20), (20, 10))
    armour = ((150, 100), (120, 80), (90, 60), (60, 40), (30, 20))
    boots = ((120, 15), (96, 12), (72, 9), (48, 6), (24, 3))
  
    boosts = []
    for shop in (weapons, armour, boots):
        for cost, boost in shop:
            if cost <= gold:
                boosts.append(boost)
                break
    return boosts
        
​
def max_stats(character, gold): 
    base = {'Knight': [120, 140, 6], 'Warrior': [180, 71, 8], 
            'Fairy': [71, 100, 16], 'Robot': [160, 120, 11], 
            'Giant': [160, 200, 4]}
    
    return [sum(i) for i in zip(base[character], buy_best(gold))]

