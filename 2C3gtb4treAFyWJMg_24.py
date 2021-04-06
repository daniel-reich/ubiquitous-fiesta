
def polybius(text):
    grid = [['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']]
    rev = {char: (row_idx+1, col_idx+1) for row_idx,row in enumerate(grid) for col_idx, char in enumerate(row)}
    rev.update({'j': rev['i'], ' ': ' '})
    text = text.lower()
    if text[0].isalpha():
        return ''.join(str(num) for char in text if char in rev for num in rev[char])
    return ' '.join(''.join([grid[int(a)-1][int(b)-1] for a,b in zip(chunk[::2],chunk[1::2])]) for chunk in text.split(' '))

