
def pascals_triangle(row):
    line = [1, 1]
    for _ in range(1, row):
        new_line = [1]
        for i in range(1, len(line)):
            new_line.append(line[i - 1] + line[i])
        new_line.append(1)
        line = new_line[:]
    return ' '.join(map(str, line))

