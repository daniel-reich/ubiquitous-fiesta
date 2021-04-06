
def cutting_grass(height,*args):
    final_height = []
    current = height
    for change in args:
        current = [a - change for a in current]
        if min(current) > 0:
            final_height.append(current)
        if min(current) <= 0:
            final_height.append("Done")
    return final_height

