
def how_mega_is_it(n):
    return "{}milestone".format("MEGA "*(len(str(int(abs(n))))-2) if abs(n)>=100 else "not a mega ")

