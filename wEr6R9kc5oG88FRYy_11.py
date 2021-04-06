
def get_frame(w, h, ch):
    if w<3 or h<3:
        return 'invalid'
    else:
        lst = [[w*ch], [w*ch]]
        lst1 = [ch + " " * (w-2) + ch]
        while h>=3:
            lst.insert(1, lst1)
            h -= 1
        return lst

