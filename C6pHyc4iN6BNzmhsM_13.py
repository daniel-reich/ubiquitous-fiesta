
def poker_hand_ranking(deck):
    rank_translation = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    tpl_lst = sorted([(rank_translation[card[:-1]]
                       if card[:-1] in rank_translation else int(card[:-1]),
                       card[-1]) for card in deck])
    ranks = list(card[0] for card in tpl_lst)
    suits = list(card[1] for card in tpl_lst)
    ranks_count = sorted([ranks.count(rank) for rank in set(ranks)])
    if len(set(suits)) == 1 and ranks == [10, 11, 12, 13, 14]:
        return 'Royal Flush'
    if len(set([tpl_lst[i][0] - tpl_lst[i - 1][0]
                for i in range(1, len(tpl_lst))])) == 1:
        if len(set(suits)) == 1:
            return 'Straight Flush'
        else:
            return 'Straight'
    if len(set(suits)) == 1:
        return 'Flush'
    if 4 in ranks_count:
        return 'Four of a Kind'
    if ranks_count == [2, 3]:
        return 'Full House'
    if 3 in ranks_count:
        return 'Three of a Kind'
    if ranks_count.count(2) == 2:
        return 'Two Pair'
    if 2 in ranks_count:
        return 'Pair'
    return 'High Card'

