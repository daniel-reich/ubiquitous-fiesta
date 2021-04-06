
def how_mega_is_it(n):
    n = abs(n)
    if n < 100:
        return "not a mega milestone"
    else: 
        x = "MEGA "
        return (len(str(int(n))) - 2) * x + "milestone"

