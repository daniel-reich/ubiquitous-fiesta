
# Check the Resources tab for the list of characters and items.
def max_stats(character, gold):
    '''
    Returns a list of the attack power, defence and speed based on this
    character's starting values and the amount of gold input, based on the list
    of characters and items above.
    '''
    CHARACTERS = {
                  'Knight': (120, 140, 6),
                  'Warrior' : (180, 71, 8),
                  'Fairy' : (71, 100, 16),
                  'Robot' : (160, 120, 11),
                  'Giant' : (160, 200, 4)
                 } # Character and their innate attack, defence and speed powers
    
    WEAPONS = {
               'Simple Sword': (10, 20),
         'Katana': (20, 40),
         'Sharpened Sword': (30, 60),
         'Great Sword': (40, 80),
         'Forgotten Sword': (50, 100)
              }   # weapons and their attack strength, cost.
​
    ARMOUR = {
              'Bronze Armor': (20, 30),
        'Iron Armor': (40, 60),
        'Steel Armor': (60, 90),
        'Obsidian Armor': (80, 120),
        'Dragonhide Armor': (100, 150)
             }  # defensive armour and their defensive power, cost
​
    BOOTS = {
             'Simple Boots': (3, 24),
       'Leather Boots': (6, 48),
       'Strong Boots': (9, 72),
       'Compound Boots': (12, 96),
       'Soft Boots': (15, 120)
            }  # footwear and their speed and cost
​
    attack, defence, speed = CHARACTERS[character]
    starters = (attack, defence, speed)  # innate attack, defence, speed
    items = (WEAPONS, ARMOUR, BOOTS)
​
    return [starters[i] + max(items[i][item][0] for item in items[i] \
                              if items[i][item][1] <= gold) \
                              for i in range(len(starters))]

