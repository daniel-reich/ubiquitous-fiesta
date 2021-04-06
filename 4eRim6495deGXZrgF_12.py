
def column_chart(productA, productB, target):
    Ymax = max(target) + 10
    H = Ymax//10 + 1
    cols = [[' ']*H]*19
    cols[0] = [str(t) for t in range(Ymax, 0, -10)] + ['  ']
    cols[2], cols[18] = [['|']*H]*2
    for day in range(7):
        col = [['Mo','Tu','We','Th','Fr','Sa','Su'][day]]
        col += ['++']*(productA[day]//10) + ['**']*(productB[day]//10)
        col += ['  ']*(target[day]//10 - len(col) + 1) + ['__']
        cols[day*2 + 4] = (col + ['  ']*(H-len(col)))[::-1]
    trans = list(zip(*cols))
    return '\n'.join([''.join(row) for row in trans])

