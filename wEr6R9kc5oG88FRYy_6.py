
def get_frame(w, h, ch):
    if (w<=2) | (h<=2):
        return 'invalid'
    else:
        nl1=[]
        
        for i in range(h):
            if (i ==0) | (i==(h-1)):
                nl1.append([ch * w])
            else:
                nl1.append([ch +' ' * (w-2)+ch])
    return nl1

