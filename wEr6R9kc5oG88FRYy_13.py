
def get_frame(w, h, ch): 
    if w<=2 or h<=2:
        return "invalid"
    return [[w*ch]]+[[ch+" "*(w-2)+ch] for i in range(h-2)]+[[w*ch]]

