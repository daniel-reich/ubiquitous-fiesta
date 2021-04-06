
def grayscale(lst):
    for row in lst:
        for c, p_lst in enumerate(row):
            val = round(sum(x if x < 256 else 255 for x in p_lst if x > 0) / 3)
            row[c] = [val] * 3
    return lst

