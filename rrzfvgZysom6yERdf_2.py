
def poker_hand_ranking(deck):
    rank_translation = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    tpl_lst = sorted([(rank_translation[card[:-1]]
                       if card[:-1] in rank_translation else int(card[:-1]),
                       card[-1]) for card in deck])
    ranks = list(card[0] for card in tpl_lst)
    suits = list(card[1] for card in tpl_lst)
    ranks_count = sorted([ranks.count(rank) for rank in set(ranks)])
    cards = sorted(set(ranks), key=lambda c: (ranks.count(c), c),
                   reverse=True)
​
    if len(set(suits)) == 1 and ranks == [10, 11, 12, 13, 14]:
        return [10]    # 'Royal Flush'
    if len(set([tpl_lst[i][0] - tpl_lst[i - 1][0]
                for i in range(1, len(tpl_lst))])) == 1:
        if len(set(suits)) == 1:
            return [9] + cards    # 'Straight Flush'
        else:
            return [5] + cards    # 'Straight'
    if len(set(suits)) == 1:
        return [6] + cards    # 'Flush'
    if 4 in ranks_count:
        return [8] + cards    # 'Four of a Kind'
    if ranks_count == [2, 3]:
        return [7] + cards    # 'Full House'
    if 3 in ranks_count:
        return [4] + cards    # 'Three of a Kind'
    if ranks_count.count(2) == 2:
        return [3] + cards    # 'Two Pairs'
    if 2 in ranks_count:
        return [2] + cards    # 'Pair'
    return [1] + cards    # 'High Card'
​
​
def player1_wins(lst):
    return sum(poker_hand_ranking(s.split()[:5]) >
               poker_hand_ranking(s.split()[5:]) for s in lst)

