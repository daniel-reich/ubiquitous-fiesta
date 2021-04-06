
def poker_hand_ranking(hand):
    hl, sl, dl, cl, e = [], [], [], [], []
    total = [hl, sl, dl, cl]
    for x in range(len(hand)): hand[x] = hand[x].replace("A", "14").replace("K", "13").replace("Q", "12").replace("J", "11")
    flush,toak,pair = False,False,False
    for a in hand:
        e.append(int(a[:-1]))
        if a[-1] == "h": hl.append(int(a[:-1]))
        elif a[-1] == "s": sl.append(int(a[:-1]))
        elif a[-1] == "d": dl.append(int(a[:-1]))
        elif a[-1] == "c": cl.append(int(a[:-1]))
    for l in total:
        l.sort()
        if len(l) == 5:
            if l[0] == 10 and l[4] == 14: return "Royal Flush"
            if l == list(range(l[0],l[4]+1)): return "Straight Flush"
            flush = True
    for x in e:
        if e.count(x) == 4: return "Four of a Kind"
    for x in e:
        if e.count(x) == 3: toak = True
    for x in e:
        if e.count(x) == 2: pair = True
    if toak and pair: return "Full House"
    if flush: return "Flush"
    e.sort()
    if e == list(range(e[0],e[4]+1)): return "Straight"
    if toak: return "Three of a Kind"
    if pair:
        pair = False
        for x in e:
            if e.count(x) == 2:
                if pair: return "Two Pair"
                pair = True
                e.remove(x)
    if pair: return "Pair"
    return "High Card"

