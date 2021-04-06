
def bonus(days):
    if days <= 32:
        return 0
    elif 32 < days <= 40:
        days = days - 32
        return days*325
    elif 40 < days <= 48:
        return 8*325+((days-40)*550)
    elif days > 48:
        return 8*325 + 8*550 +((days-48)*600)

