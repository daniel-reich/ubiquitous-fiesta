
def left_slide(row):
    og_len = len(row)
    row = [v for v in row if v != 0]
    for i in range(len(row)):
        try:
            if row[i] == row[i + 1]:
                row[i] += row[i]
                row.pop(i + 1)
        except IndexError:
            pass
    return row + [0 for i in range(og_len - len(row))]

