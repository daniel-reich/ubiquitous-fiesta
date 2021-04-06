
def bonus(days):
    if days>48:
        x=days-(32+8+8)
        return 32*0+8*325+8*550+x*600
    elif 40<=days and days<=48:
        x=days-(32+8)
        return 32*0+8*325+x*550
    elif 32<days and days<=40:
        x=days-32
        return 32*0+x*325
    else:
        return 0

