
def million_in_month(first_month, multiplier):
    savings = first_month
    i = 1
    while savings <= 1000000:
        first_month = first_month*multiplier
        savings += first_month
        
        i += 1
        
    return i

