
characters = { 'Knight': (120, 140, 6),
        'Warrior': (180, 71 , 8), 
        'Fairy': (71, 100, 16),
        'Robot': (160, 120, 11), 
        'Giant': (160, 200, 4) }
​
def max_stats(character, gold):
    weap = min((gold//20)*10, 50)
    armor = min((gold//30)*20, 100)
    boot = min((gold//24)*3, 15)
    attack, defense, speed = characters[character]
    return [weap+attack, armor+defense, boot+speed]

