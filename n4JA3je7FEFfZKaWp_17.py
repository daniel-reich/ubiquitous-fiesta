
def million_in_month(first, mult):
    bal=first
    count=1
    while bal<1000000:
        bal=bal*mult + first
        count+=1
    return count

