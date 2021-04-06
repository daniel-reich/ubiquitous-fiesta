
def get_coin_balances(lst1, lst2):
    cnt1, cnt2 = 3, 3
    for i in range(len(lst1)):
        if lst1[i] == 'share':
            cnt1 -= 1
            cnt2 += 3           
        if lst2[i] == 'share':
            cnt2 -= 1
            cnt1 += 3
    return [cnt1, cnt2]

