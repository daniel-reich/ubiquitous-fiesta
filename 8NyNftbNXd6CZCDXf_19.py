
def get_coin_balances(lst1, lst2):
    A = 3;
    B = 3;
    for a,b in zip(lst1,lst2):
        if a == 'share' and b == 'share':
            A += 2;
            B += 2;
        elif a == 'steal' and b == 'share':
            A += 3;
            B -= 1;
        elif a == 'share' and b == 'steal':
            A -= 1;
            B += 3;
        elif a == 'steal' and b == 'steal':
            A += 0;
            B += 0;
        else:
            return "FATAL ERROR!"
    return [A,B];

