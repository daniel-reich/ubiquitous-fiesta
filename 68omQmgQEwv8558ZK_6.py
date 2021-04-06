
def max_stats(character, gold):
    characters = {
        'Knight' : [120, 140, 6],
        'Warrior' : [180, 71, 8],
        'Fairy' : [71, 100, 16],
        'Robot' : [160, 120, 11],
        'Giant' : [160, 200, 4]
    }
    weapons = {
        'Simple Sword': [10, 20],
        'Katana': [20, 40],
        'Sharpened Sword': [30, 60],
        'Great Sword': [40, 80],
        'Forgotten Sword': [50, 100]
    }
    armor = {
        'Bronze Armor': [20, 30],
        'Iron Armor': [40, 60],
        'Steel Armor': [60, 90],
        'Obsidian Armor': [80, 120],
        'Dragonhide Armor': [100, 150]
    }
    boots = {
        'Simple Boots': [3, 24],
        'Leather Boots': [6, 48],
        'Strong Boots': [9, 72],
        'Compound Boots': [12, 96],
        'Soft Boots': [15, 120]
    }
    add_attack =  [i[0] for i in weapons.values() if i[1]==max([i[1] for i in weapons.values() if i[1] <= gold])]
    add_defense = [i[0] for i in armor.values() if i[1]==max([i[1] for i in armor.values() if i[1] <= gold])]
    add_speed = [i[0] for i in boots.values() if i[1]==max([i[1] for i in boots.values() if i[1] <= gold])]
    return [
    characters[character][0] + add_attack[0],
    characters[character][1] + add_defense[0],
    characters[character][2] + add_speed[0]
    ]

