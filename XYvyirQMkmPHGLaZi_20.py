
def boom_intensity(n):
    return "B{}M!".format("O"*n) if not n%10 and n>=2 else "B{}M".format("O"*n) if not n%5 and n>=2 else "B{}m!".format("o"*n) if not n%2 and n>=2 else "B{}m".format("o"*n) if n>=2 else "boom"

