
def shortest_path(lst):
    pos, max_char = dict(), 0
    for r, tpl in enumerate(lst):
        for c, char in enumerate(tpl):
            if char in '123456789':
                pos[int(char)] = (r, c)
                if int(char) > max_char:
                    max_char = int(char)
    return sum(abs(pos[i][1] - pos[i - 1][1]) + abs(pos[i][0] - pos[i - 1][0])
               for i in range(2, max_char + 1))

