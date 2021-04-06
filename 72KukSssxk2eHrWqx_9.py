
def char_at_pos(r, s):
    if s == 'even':
        if isinstance(r, str):
            return ''.join([r[i] for i in range(len(r)) if i % 2 == 0])
        return [r[-i] for i in range(1,len(r)+1) if i % 2 == 0][::-1]
    elif s == 'odd':
        if isinstance(r, str):
            return ''.join([r[i] for i in range(len(r)) if i % 2 != 0])
        return [r[-i] for i in range(1,len(r)+1) if i % 2 != 0][::-1]

