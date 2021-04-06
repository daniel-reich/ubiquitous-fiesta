
def poker_hand_ranking(hand):
    def compare(elem):
            return rank[elem]
    hands=["Royal Flush","Straight Flush","Four of a Kind","Full House","Flush","Straight","Three of a Kind","Two Pair","Pair","High Card"]
    rank=list("23456789")+["10"]+list("JQKA")
    rank=dict(enumerate(rank))
    rank = {y:x for x,y in rank.items()}
    suits=[elem[-1] for elem in hand]
    ranks=[elem[:-1] for elem in hand]
    ranks=sorted (ranks, key = compare)
    suit_freq = {x:suits.count(x) for x in suits}
    rank_freq = {x:ranks.count(x) for x in ranks}
    if len(rank_freq)==2 and max(rank_freq.values())==4:
        return hands[2]
    elif len(rank_freq)==2 and max(rank_freq.values())==3:
        return hands[3]
    elif len(rank_freq)==3 and max(rank_freq.values())==3:
        return hands[6]
    elif len(suit_freq)==1 and all([1 if rank in ["A","Q","K","J","10"] else 0 for rank in ranks]):
        return hands[0]
    elif len(suit_freq)==1 :                
        if all([1 if rank[ranks[index]]==rank[ranks[index+1]]-1 else 0  for index in range(4)]):
            return hands[1]
        else:
            return hands[4]
    elif all([1 if rank[ranks[index]]==rank[ranks[index+1]]-1 else 0  for index in range(4)]):
        return hands[5]
    elif  len(suit_freq)==1 :
        return hands[4]
    elif len (rank_freq)==3:
        return hands[7]
    elif len(rank_freq)==4:
        return hands[8]
    else:
        return hands[9]

