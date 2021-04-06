
def get_frame(w, h, ch):
    lst = []
    if w <= 2 or h <= 2:
        return 'invalid'
    for i in range(h):
        if i == 0 or i == h-1:
            lst.append([ch * w])
        else:
            lst.append([ch + ' ' * (w-2) + ch])        
    return lst

