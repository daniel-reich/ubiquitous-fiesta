
def calculate_damage(your_type, opponent_type, attack, defense):
    damage = 50 * (attack / defense)
    d1= {"firegrass":2,"grasswater":2,"electricwater":2,"grasselectric":1,"fireelectric":1,"electricfire":1,"electricgrass":1}
    if your_type + opponent_type in d1:
        effectiveness = d1[your_type + opponent_type] 
    elif your_type==opponent_type:
        effectiveness = 1
    else:
        effectiveness = 0.5
    return int(damage*effectiveness)

