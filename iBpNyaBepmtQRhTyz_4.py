
def c_cipher(msg, keyword):
    if msg.islower():
        order = sorted(keyword)
        rows = len(msg)//len(keyword)
        groups = [msg[i::rows] for i in range(rows)]
        return ''.join(''.join(group[order.index(i)] for i in keyword) for group in groups)
    else:
        order = sorted(enumerate(keyword), key=lambda x: x[1])
        msg = ''.join(i for i in msg.lower() if i.isalnum())
        gap = len(msg)%len(keyword)
        if gap != 0:
            msg += 'x' * (len(keyword) - gap)
        return ''.join(msg[idx::len(keyword)] for idx, _ in order)

