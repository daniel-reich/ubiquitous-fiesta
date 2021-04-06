
d = {'people' : 10, "walls" : 10, "minutes" : 22}
def time(d, people, walls):
    rate = (d["walls"] / d["minutes"]) / d["people"]
    minutes = ((1/rate) / people) * walls
    return minutes

