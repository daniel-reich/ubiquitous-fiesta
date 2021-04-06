
def binary_clock(time):
    row, result = [], []
    for ch in (time.replace(':', '')):
        row.append(list(bin(int(ch))[2:][::-1])+(4-len(bin(int(ch))[2:]))*['0'])
        row[-1].reverse()
    for r in range(4):
        result.append(''.join(row[y][r] for y in range(6)))
    result[0] = ' '+result[0][1]+' '+result[0][3]+' '+result[0][5]
    result[1] = ' '+result[1][1:] 
    return result

