
def first_repeat(chars):
    hist = {}
    for char in chars:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
        
    for k,v in hist.items():
        if v > 1:
            return k  
    return str(-1)

