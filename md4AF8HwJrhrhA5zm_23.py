
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow",
               "yellow-green", "green", "blue-green", "blue", "blue-violet",
               "violet", "red-violet"]
    res, begin_idx = [], colours.index(anchor)
    if combination == 'complementary':
        for i in [0, 6]:
            res.append(colours[(begin_idx + i) % 12])
    elif combination == 'analogous':
        for i in [0, 1, -1]:
            res.append(colours[(begin_idx + i) % 12])
    elif combination == 'triadic':
        for i in [0, 4, 8]:
            res.append(colours[(begin_idx + i) % 12])
    elif combination == 'split_complementary':
        for i in [0, 5, 7]:
            res.append(colours[(begin_idx + i) % 12])
    elif combination == 'rectangle':
        for i in [0, 2, 6, 8]:
            res.append(colours[(begin_idx + i) % 12])
    elif combination == 'square':
        for i in [0, 3, 6, 9]:
            res.append(colours[(begin_idx + i) % 12])
    return set(res)

