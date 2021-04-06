
def over_time(lst, half_up_round=0.001):
    checkin, checkout, rate, ot_multi = lst
    regular = max(min(17, checkout) - max(9, checkin), 0) * rate
    extra = max(checkout - max(17, checkin), 0) * rate * ot_multi
    return '${0:.2f}'.format(regular + extra + half_up_round, 2)

