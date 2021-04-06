
def pH_name(pH):
    if pH>0 and pH<7:
        return 'acidic'
    elif pH>7 and pH<14:
        return 'alkaline'
    elif pH==7:
        return 'neutral'
    else:
        return 'invalid'

