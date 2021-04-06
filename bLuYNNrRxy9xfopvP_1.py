
def yahtzee_score_calc(lst):
    scores = [sum(dice.count(i)*i for i, dice in enumerate(lst[:6], 1)), # Singles
              sum(lst[6]) * any(lst[6].count(i) >= 3 for i in lst[6]), # Three of a Kind 
              sum(lst[7]) * any(lst[7].count(i) >= 4 for i in lst[7]), # Four of a Kind
              25 * (len(set(lst[8])) == 2), # Full House
              30 * any(i.issubset(set(lst[9])) for i in ({1,2,3,4}, {2,3,4,5}, {3,4,5,6})), # Low Straight
              40 * any(i.issubset(set(lst[10])) for i in ({1,2,3,4,5}, {2,3,4,5,6})), # High Straight
              50 * (len(set(lst[11])) == 1), # Yahtzee
              sum(lst[12])] # Chance
​
    total = sum(scores)
    return total + 35 if scores[0] >= 63 else total

