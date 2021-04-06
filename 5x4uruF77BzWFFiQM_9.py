
def pH_name(pH):
    if pH <= 6.5 and pH >= 0:
        return "acidic"
    if pH > 6.5  and pH < 7.5:
        return "neutral"
    if pH >= 7.5 and pH <= 14:
        return "alkaline"
    else:
        return "invalid"

