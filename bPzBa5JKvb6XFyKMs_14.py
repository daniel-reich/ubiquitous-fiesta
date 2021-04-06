
def get_primiera_score(deck):
    card_points = {'A': 16, '6': 18, '7': 21,
                   '2': 12,'3': 13, '4': 14, '5': 15,
                   'J': 10, 'Q': 10, 'K': 10}
    suits = ('d', 'h', 's', 'c')
    pts = [[card_points.get(card[0], 0) for card in deck if card[1] == suit] for suit in suits]
    if all([len(suit_pts) > 0 for suit_pts in pts]):
        return sum([max(suit_pts) for suit_pts in pts])
    return 0

