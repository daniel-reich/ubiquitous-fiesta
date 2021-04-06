
def EPLResult(table, team):
    for i in range(len(table)):
        table[i].append(3 * table[i][2] + table[i][3])
    table.sort(key=lambda x: (-x[6], -x[5]))
    pos = 0
    for t in table:
        pos += 1
        if t[0] == team:
            ans = team + " came " + str(pos)
            ans += "st" if pos == 1 else ("nd" if pos == 2 else ("rd" if pos == 3 else "th"))
            ans += " with " + str(t[-1]) + " points and a goal difference of " + str(t[5]) + "!"
            return ans

