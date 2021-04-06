
def pilish_string(s):
    if not s:
        return s
    lengths = [int(x) for x in '314159265358979']
    i = 0
    ws = []
    for l in lengths:
        if i+l <= len(s):
            ws.append(s[i:i+l])
        else:
            ws.append(s[i:] + s[-1]*(i+l-len(s)))
        i += l
        if i >= len(s):
            break
    return ' '.join(ws)

