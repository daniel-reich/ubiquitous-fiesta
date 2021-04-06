
def chocolates_parcel(n_small, n_big, order):
    RequiredSmall = 0
    if not(order%2):   
        while n_big > 1 and order >= 10:
            n_big -= 2
            order -= 10
        while n_small > 0 and order >= 2:
            n_small -= 1
            order -= 2
            RequiredSmall += 1
        if order == 0:
            return RequiredSmall
        return -1
    else:
        order -= 5
        n_big -= 1
        while n_big > 1 and order >= 10:
            n_big -= 2
            order -= 10
        while n_small > 0 and order >= 2:
            n_small -= 1
            order -= 2
            RequiredSmall += 1
        if order == 0:
            return RequiredSmall
        return -1
def chocolates_parcel(n_small, n_big, order):
    RequiredSmall = 0
    if not(order%2):   
        while n_big > 1 and order >= 10:
            n_big -= 2
            order -= 10
        while n_small > 0 and order >= 2:
            n_small -= 1
            order -= 2
            RequiredSmall += 1
        if order == 0:
            return RequiredSmall
        return -1
    else:
        if n_big != 0:
            order -= 5
            n_big -= 1
        while n_big > 1 and order >= 10:
            n_big -= 2
            order -= 10
        while n_small > 0 and order >= 2:
            n_small -= 1
            order -= 2
            RequiredSmall += 1
        if order == 0:
            return RequiredSmall
        return -1

