
def EPLResult(input_table, team):
    tbl = [(i[2] * 3 + i[3], i[5], i[0]) for i in input_table]
    tbl.sort(key=lambda t: (-t[0], -t[1]))
    idx = 0
    while tbl[idx][2] != team:
        idx += 1
    place = ["1st", "2nd", "3rd"][idx] if idx < 3 else "{}th".format(idx + 1)
    return ("{} came {} with {} points and a goal difference of {}!"
            .format(tbl[idx][2], place, tbl[idx][0], tbl[idx][1]))

