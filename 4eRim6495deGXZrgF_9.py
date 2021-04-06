
def column_chart(productA, productB, target):
    total = [productA[i] + productB[i] for i in range(7)]
    M = max(max(total), max(target))
    rows = []
    perc = 10
    while perc <= M + 10:
        row = [str(perc), '|']
        for i in range(7):
            a, b, t = productA[i], productB[i], target[i]
            if perc <= a:
                row.append('++')
            elif perc <= a + b:
                row.append('**')
            elif perc == t + 10:
                row.append('__')
            else:
                row.append('  ')
        row.append('|')
        rows.append(' '.join(row))
        perc += 10
    rows = rows[::-1]
    rows.append('   | Mo Tu We Th Fr Sa Su |')
    return '\n'.join(rows)

