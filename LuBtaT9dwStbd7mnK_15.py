
def tallest_building_height(r):
    for i,v in enumerate(r):
        if "#" in v: return str((len(r) - i) * 20) + "m"

