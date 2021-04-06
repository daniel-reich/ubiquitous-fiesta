
def swap_two(txt):
    if not len(txt) % 4:
        nl = [txt[i:i+4] for i in range(0, len(txt), 4)]
        return ''.join(w[2]+w[3]+w[0]+w[1] for w in nl)
    else:
        nl = [txt[i:i+4] for i in range(0, len(txt)//4*4, 4)]
        return ''.join(w[2]+w[3]+w[0]+w[1] for w in nl)+txt[len(txt)//4*4:]

