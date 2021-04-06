
d = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'GR': 'B', 'RB': 'G', 'BR': 'G', 'GB': 'R', 'BG': 'R'}
​
def coloured_triangle(row):
    if len(row) == 1:
        return row
    else:
        txt = [row[i:i + 2] for i in range(len(row) - 1)]
        for j in txt:
            row = "".join(j.replace(j, d[j]))
            return coloured_triangle(row)

