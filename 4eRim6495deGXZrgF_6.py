
def column_chart(productA, productB, target):
    res = ''
    target = [x + 10 for x in target]
    for row in range(max(target), 0, -10):
        daily_marks = ''
        for day in range(7):
            if target[day] == row:
                daily_marks += '__ '
            elif productA[day] < row <= productA[day] + productB[day]:
                daily_marks += '** '
            elif row <= productA[day]:
                daily_marks += '++ '
            else:
                daily_marks += '   '
        res += str(row) + ' | {}|\n'.format(daily_marks)
    res += '   | Mo Tu We Th Fr Sa Su |'
    return res

