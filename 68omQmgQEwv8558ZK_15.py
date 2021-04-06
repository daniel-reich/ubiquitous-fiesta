
dictionary_character = {"Knight":[120, 140, 6],
  "Warrior" : [180, 71, 8],
  "Fairy" : [71, 100, 16],
  "Robot" : [160,120, 11],
    "Giant" : [160, 200, 4]
    }
    
dictionary_weapon = {
    10:20,
  20:40,
    30:60,
  40:80,
    50:100}
​
dictionary_armor = {
        20:30,
        40:60,
        60:90,
        80:120,
        100:150       
        }
dictionary_boots = {
        3:24,
        6:48,
        9:72,
        12:96,
        15:120        
        }
​
def max_stats(character,gold):
    final = []
    temp_weapon = []
    temp_boots = []
    temp_armor = []
    for x,y in dictionary_weapon.items():
        temp_weapon.append(y)
        temp_weapon.sort(reverse=True)
    for weapon in temp_weapon:
        if weapon > gold:
            continue
        if weapon <= gold:
            for x,y in dictionary_weapon.items():
                if y == weapon:
                    final.append(x)
        break
    for x,y in dictionary_armor.items():
        temp_armor.append(y)
        temp_armor.sort(reverse=True)
    for armor in temp_armor:
        if armor > gold:
            continue
        if armor <= gold:
            for x,y in dictionary_armor.items():
                if y == armor:
                    final.append(x)
        break
    for x,y in dictionary_boots.items():
        temp_boots.append(y)
        temp_boots.sort(reverse=True)
    for boots in temp_boots:
        if boots > gold:
            continue
        if boots <= gold:
            for x,y in dictionary_boots.items():
                if y == boots:
                    final.append(x)
        break
    
    character_pow = dictionary_character[character]
    
    for i in range(0,3):
        character_pow[i] += final[i]
    
    return character_pow

