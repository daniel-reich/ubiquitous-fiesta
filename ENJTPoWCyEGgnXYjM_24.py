
def percent_filled(box):
    ttl_spaces,ttl_filled = 0,0
    for row in box:
        spaces = len([i for i in row if i != "#"])
        filled = len([i for i in row if i == "o"])
        ttl_spaces += spaces
        ttl_filled += filled
    if ttl_filled:
        return str(round((ttl_filled/ttl_spaces)*100))+"%"
    return "0%"

