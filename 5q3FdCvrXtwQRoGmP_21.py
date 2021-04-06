
def count_towers(towers):
    base_count = 0
    for i in str(towers[-1]):
        if i == '#':
            base_count += 1
    return base_count / 2

