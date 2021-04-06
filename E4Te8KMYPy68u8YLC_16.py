
def volume_of_box(sizes):
    values = sizes.values()
    prod = 1
    for i in values:
        prod *=i
    return prod

