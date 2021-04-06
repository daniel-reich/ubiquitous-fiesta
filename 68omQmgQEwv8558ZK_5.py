
def max_stats(character, gold):
    attack, defense, speed = 0, 1, 2
    value, gold_idx = 0, 1
    characters = {'Knight': [120, 140, 6],
                  'Warrior': [180, 71, 8],
                  'Fairy': [71, 100, 16],
                  'Robot': [160, 120, 11],
                  'Giant': [160, 200, 4]}
    weapons = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100]]
    armor = [[20, 30], [40, 60], [60, 90], [80, 120], [100, 150]]
    boots = [[3, 24], [6, 48], [9, 72], [12, 96], [15, 120]]
    result = characters[character]
    idx = -1
    while idx < 4:
        if weapons[idx + 1][gold_idx] <= gold:
            idx += 1
        else:
            break
    if idx > -1:
        result[attack] += weapons[idx][value]
    idx = -1
    while idx < 4:
        if armor[idx + 1][gold_idx] <= gold:
            idx += 1
        else:
            break
    if idx > -1:
        result[defense] += armor[idx][value]
    idx = -1
    while idx < 4:
        if boots[idx + 1][gold_idx] <= gold:
            idx += 1
        else:
            break
    if idx > -1:
        result[speed] += boots[idx][value]
    return result

