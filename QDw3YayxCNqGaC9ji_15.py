
def make_change(c):
    change = {}
    change["q"] = c//25
    change["d"] = (c - (change["q"] * 25))//10
    change["n"] = (c - ((change["q"] * 25) + (change["d"] * 10))) // 5
    change["p"] = (c - ((change["q"] * 25) + (change["d"] * 10) + change["n"] * 5))
    return change

