
def pH_name(pH):
    if pH ==7:
        return 'neutral'
    elif 7<pH<14:
        return 'alkaline'
    elif 0<pH<7:
        return 'acidic'
    else:
        return "invalid"

