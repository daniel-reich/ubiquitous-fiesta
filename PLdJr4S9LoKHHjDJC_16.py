
def identify(*cube):
    
    height = len(cube)
    width = max(len(c) for c in cube)
    count_chr = sum(c.count("O") for c in cube)
​
    if count_chr != height * width: return "Missing " + str(height * width - count_chr)
    return "Non-Full" if height != width else "Full"

