
def get_frame(w, h, ch):
    list = []
    if w <= 2 or h <= 2:
        return 'invalid'
    for i in range(h):
        if i == 0 or i == h-1:
            list.append([ch*w])
        else:
            list.append([ch + ' '*(w-2) + ch])
    return list

