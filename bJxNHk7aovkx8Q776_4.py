
def gold_distribution(gold):
    matt = []
    mm = []
    while gold != []:
        if gold[0] > gold[-1]:
            if len(matt) == len(mm):
                matt.append(gold[0])
            else:
                mm.append(gold[0])
            gold = gold[1:]
        elif gold[-1] > gold[0]:
            if len(matt) == len(mm):
                matt.append(gold[-1])
            else:
                mm.append(gold[-1])
            gold = gold[:-1]
        else:
            if len(matt) == len(mm):
                matt.append(gold[0])
            else:
                mm.append(gold[0])
            gold = gold[1:]
    return [sum(matt),sum(mm)]

