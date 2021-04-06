
def char_at_pos(r, s):
    if type(r)==list:
        if s=='even':
            return [r[i] for i,j in enumerate(r) if i%2!=0] 
        else:
            return [r[i] for i in range(len(r)) if i%2==0]
    else:
        if s=='even':
            return ''.join([r[i] for i,j in enumerate(r) if i%2!=0]) 
        else:
            return ''.join([r[i] for i in range(len(r)) if i%2==0])

