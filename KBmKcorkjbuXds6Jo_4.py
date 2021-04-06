
def chocolates_parcel(n_small, n_big, order):
    order -= 5 * min(n_big, order // 5)
    while order > 0:
        if not order % 2:
            req_small = order // 2
            if req_small <= n_small:
                return req_small
            else:
                return -1
        else:
            order += 5
    return 0

