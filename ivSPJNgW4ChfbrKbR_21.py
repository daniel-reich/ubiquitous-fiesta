
def soroban(frame):
    res = ''
    for i in zip(*frame):
        res += str((5 if i[1] == 'O' else 0) + i[3:].index('|'))
    return int(res)

