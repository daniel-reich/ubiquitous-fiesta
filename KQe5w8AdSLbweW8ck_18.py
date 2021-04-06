
def char_at_pos(r, s):
    return [r[i] for i in range(len(r)) if (i+1)%2 == 0] if s== "even" and isinstance(r,list) else [r[i] for i in range(len(r)) if (i+1)%2 == 1] if isinstance(r,list) else "".join([r[i] for i in range(len(r)) if (i+1)%2 == 0]) if s== "even" and isinstance(r,str) else "".join([r[i] for i in range(len(r)) if (i+1)%2 == 1])

