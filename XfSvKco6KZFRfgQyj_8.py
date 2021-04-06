
def find_a_seat(n, lst):
    for i,v in enumerate(lst):
        if (v/(n/len(lst)))*100<=50:return i
    return -1

