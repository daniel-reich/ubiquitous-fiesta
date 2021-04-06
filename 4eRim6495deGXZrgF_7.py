
def column_chart(productA, productB, target):
    height = max(target)//10
    blank_col = [' '] * (height + 1)
    axis_line = ['|'] * (height + 1)
    
    chart = [[str(i) for i in range(10, max(target) + 11, 10)]]
    chart.append(blank_col)
    chart.append(axis_line)
    chart.append(blank_col)
​
    for a, b, t in zip(productA, productB, target):
        a, b, t = a//10, b//10, t//10
        column = ['+']*a + ['*']*b + [' ']*(t - a - b ) + ['_'] + [' ']*(height - t)
        chart.append(column)
        chart.append(column)
        chart.append(blank_col)
​
    chart.append(axis_line)
    res = '\n'.join([''.join(i) for i in zip(*chart)][::-1]) + '\n' + '   | Mo Tu We Th Fr Sa Su |'
​
    return res

