
def check_flush(table, hand):
    cards=table+hand
    cards=set(cards)
    flush=[]
    number=[]
    for string in cards:
        if (''.join(cards)).count(string[-1])>=5:
            flush.append(string)
    if len(flush)<5:
        return False
    return True

