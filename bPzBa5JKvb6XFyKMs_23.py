
def valid(lst):
    d = {'c': 0,'d': 0,'h': 0, 's':0}
    for card in lst:
        suit = card[1]
        if suit in d:
            d[suit] += 1
    return False if min(d.values()) == 0 else True
​
def maxCard(lst,dict):
    if len(lst) == 1:
        if lst[0] in dict:
            if(lst[0][0].isdigit() and int(lst[0][0]) >= 2 and int(lst[0][0]) <= 5):
                return dict[lst[0]] + int(lst[0][0])
            else:
                return dict[lst[0]]
    else:
        card_scores = {}
        for card in lst:
            if(card[0].isdigit() and int(card[0]) >= 2 and int(card[0]) <= 5):
                card_scores[card] = dict[card] + int(card[0])
            else:
                card_scores[card] = dict[card]
​
        return max(card_scores.values())
​
def get_primiera_score(lst):
    #clubs, diamonds, herats, spades
    points_scale = {
    '2c': 10, '3c': 10, '4c': 10, '5c': 10, '6c': 18, '7c': 21, 'Ac': 16, 'Jc': 10, 'Kc': 10, 'Qc': 10,
    '2d': 10, '3d': 10, '4d': 10, '5d': 10, '6d': 18, '7d': 21, 'Ad': 16, 'Jd': 10, 'Kd': 10, 'Qd': 10,
    '2h': 10, '3h': 10, '4h': 10, '5h': 10, '6h': 18, '7h': 21, 'Ah': 16, 'Jh': 10, 'Kh': 10, 'Qh': 10,
    '2s': 10, '3s': 10, '4s': 10, '5s': 10, '6s': 18, '7s': 21, 'As': 16, 'Js': 10, 'Ks': 10, 'Qs': 10 }
​
    clubs = []
    diamonds = []
    hearts = []
    spades = []
​
    if(not valid(lst)):
        return 0
    else:
        #calculate the primiera score
        for card in lst:
            if(card.endswith('c')):
                clubs.append(card)
            elif(card.endswith('d')):
                diamonds.append(card)
            elif(card.endswith('h')):
                hearts.append(card)
            elif(card.endswith('s')):
                spades.append(card)
​
        scores = [maxCard(clubs,points_scale), maxCard(diamonds,points_scale), maxCard(hearts,points_scale), maxCard(spades,points_scale)]
​
    return sum(scores)

