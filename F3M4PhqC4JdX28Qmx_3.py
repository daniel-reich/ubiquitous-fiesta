
def back_to_home(directions):
    x = 0
    y = 0
    for a in directions:
        if "N" in a:
            x += 1
        elif "W" in a:
            y -= 1
        elif "S" in a:
            x -= 1
        elif "E" in a:
            y += 1
    if x == 0 and y == 0:
        return True
    else:
        return False
print(back_to_home("NENESSWW"))

