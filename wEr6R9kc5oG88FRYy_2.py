
def get_frame(w, h, ch):
    if w < 3 or h < 3:
        return 'invalid'
    result = [[ch * w]]
    for i in range(h - 2):
        result.append([ch + (w - 2) * ' ' + ch])
    result.append([ch * w])
    return result

