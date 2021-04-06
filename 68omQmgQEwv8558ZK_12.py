
def max_stats(character, gold):
    Characters = {'Knight' : (120, 140, 6), 'Warrior' : (180 , 71 , 8 ), 'Fairy' : (71 , 100 , 16 ), 'Robot' : (160 , 120 , 11), 'Giant' : (160 , 200 , 4)}
    Attack = {'SimpleSword': (10, 20), 'Katana': (20, 40), 'SharpenedSword': (30, 60), 'GreatSword': (40, 80), 'ForgottenSword': (50, 100)}
    Defense = {'BronzeArmor': (20, 30), 'IronArmor': (40, 60), 'SteelArmor': (60, 90), 'ObsidianArmor': (80, 120), 'DragonhideArmor': (100, 150) }
    Speed = {'SimpleBoots': (3, 24), 'LeatherBoots': (6, 48), 'StrongBoots': (9, 72), 'CompoundBoots': (12, 96), 'SoftBoots': (15, 120)}
​
    last = Characters[character][0]
    a = sorted(Attack.values(), key= lambda x : x[1])
    for idx, attackTuple in enumerate(a):
        if attackTuple[1] > gold:
            break
        else:
            last = attackTuple[0]
    attackStrength = last + Characters[character][0]
​
    last = Characters[character][1]
    a = sorted(Defense.values(), key= lambda x : x[1])
    for idx, defenseTuple in enumerate(a):
        if defenseTuple[1] > gold:
            break
        else:
            last = defenseTuple[0]
    defenseStrength = last + Characters[character][1]
​
    last = Characters[character][2]
    a = sorted(Speed.values(), key= lambda x : x[1])
    for idx, speedTuple in enumerate(a):
        if speedTuple[1] > gold:
            break
        else:
            last = speedTuple[0]
    speedStrength = last + Characters[character][2]
​
    return [attackStrength, defenseStrength, speedStrength]

